"""
Pytest test suite for AssetManager.

No display server or real PNG files required — pygame I/O is fully stubbed.

HOW THE STUB WORKS
------------------
test_asset_manager.py imports the *real* AssetManager from your project
(from pacman.assets.asset_manager) but replaces pygame's image.load and
transform.scale with MagicMocks backed by in-memory FakeSurface objects.
The autouse fixture _reset_mocks wipes those mocks between every test.
"""
from __future__ import annotations

import types
from pathlib import Path
from unittest.mock import MagicMock
import pytest

# ---------------------------------------------------------------------------
# Import the real classes from the project (adjust path if needed)
# ---------------------------------------------------------------------------
from pacman.assets.asset_manager import AssetManager, StripKey

# ---------------------------------------------------------------------------
# Build a minimal pygame stub and PATCH it into the already-imported module
# ---------------------------------------------------------------------------


def _build_pygame_stub():
    """
    Returns a fake pygame module whose image.load and transform.scale are
    MagicMocks that never touch the filesystem.
    """

    class FakeSurface:
        def __init__(self, size=(48, 48)):
            self._size = tuple(size)
            self._pixels: dict = {}

        def get_size(self):
            return self._size

        def get_at(self, pos):
            return self._pixels.get(pos, (0, 0, 0, 255))

        def set_at(self, pos, color):
            self._pixels[pos] = tuple(color)

        def convert_alpha(self):
            return self

        def subsurface(self, rect):
            surf = FakeSurface((rect.width, rect.height))
            for (x, y), color in self._pixels.items():
                nx, ny = x - rect.x, y - rect.y
                if 0 <= nx < rect.width and 0 <= ny < rect.height:
                    surf._pixels[(nx, ny)] = color
            return surf

        def copy(self):
            s = FakeSurface(self._size)
            s._pixels = dict(self._pixels)
            return s

    class FakeRect:
        def __init__(self, x, y, w, h):
            self.x, self.y = x, y
            self.width, self.height = w, h

    pygame_stub = types.SimpleNamespace()
    pygame_stub.Surface = FakeSurface
    pygame_stub.Rect = FakeRect

    _loaded: dict = {}

    def _fake_load(path):
        if path not in _loaded:
            _loaded[path] = FakeSurface((144, 48))
        return _loaded[path]

    image_stub = types.SimpleNamespace()
    image_stub.load = MagicMock(side_effect=_fake_load)
    image_stub._loaded = _loaded
    pygame_stub.image  = image_stub

    def _fake_scale(surf, size):
        return FakeSurface(size)

    transform_stub = types.SimpleNamespace()
    transform_stub.scale = MagicMock(side_effect=_fake_scale)
    pygame_stub.transform = transform_stub

    return pygame_stub


_PG = _build_pygame_stub()

# Patch pygame inside the already-imported asset_manager module so that
# its module-level `import pygame` reference is replaced by our stub.
import pacman.assets.asset_manager as _am_mod
_am_mod.pygame = _PG          # replaces the pygame name inside that module


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def _reset_mocks():
    _PG.image.load.reset_mock()
    _PG.transform.scale.reset_mock()
    _PG.image._loaded.clear()
    yield


@pytest.fixture()
def mgr():
    return AssetManager()


@pytest.fixture()
def sheet_path(tmp_path) -> str:
    return str(tmp_path / "sheet.png")


# ---------------------------------------------------------------------------
# 1. Initial state
# ---------------------------------------------------------------------------

class TestInitialState:
    def test_sheets_cache_starts_empty(self, mgr):
        assert mgr._sheets == {}

    def test_strips_cache_starts_empty(self, mgr):
        assert mgr._strips == {}


# ---------------------------------------------------------------------------
# 2. load_sheet
# ---------------------------------------------------------------------------

class TestLoadSheet:
    def test_returns_a_surface(self, mgr, sheet_path):
        assert mgr.load_sheet(sheet_path) is not None

    def test_image_load_called_once(self, mgr, sheet_path):
        mgr.load_sheet(sheet_path)
        _PG.image.load.assert_called_once_with(sheet_path)

    def test_second_call_returns_cached(self, mgr, sheet_path):
        s1 = mgr.load_sheet(sheet_path)
        s2 = mgr.load_sheet(sheet_path)
        assert s1 is s2
        assert _PG.image.load.call_count == 1

    def test_different_paths_load_separately(self, mgr, tmp_path):
        mgr.load_sheet(str(tmp_path / "a.png"))
        mgr.load_sheet(str(tmp_path / "b.png"))
        assert _PG.image.load.call_count == 2

    def test_path_object_normalised_to_str_key(self, mgr, tmp_path):
        mgr.load_sheet(str(tmp_path / "sheet.png"))
        mgr.load_sheet(tmp_path / "sheet.png")
        assert _PG.image.load.call_count == 1

    def test_convert_alpha_called_on_raw_surface(self, mgr, sheet_path):
        raw = _PG.Surface()
        converted = _PG.Surface()
        raw.convert_alpha = MagicMock(return_value=converted)
        _PG.image.load.side_effect = lambda p: raw

        result = mgr.load_sheet(sheet_path)
        raw.convert_alpha.assert_called_once()
        assert result is converted

    def test_converted_surface_stored_in_cache(self, mgr, sheet_path):
        surf = mgr.load_sheet(sheet_path)
        assert mgr._sheets[sheet_path] is surf


# ---------------------------------------------------------------------------
# 3. get_strip
# ---------------------------------------------------------------------------

class TestGetStrip:
    def test_returns_tuple(self, mgr, sheet_path):
        assert isinstance(
            mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3),
            tuple,
        )

    def test_frame_count_matches_requested(self, mgr, sheet_path):
        for n in (1, 2, 3, 4):
            m = AssetManager()
            assert len(m.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=n)) == n

    def test_zero_frame_count_returns_empty_tuple(self, mgr, sheet_path):
        assert mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=0) == ()

    def test_cache_returns_same_object(self, mgr, sheet_path):
        s1 = mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        s2 = mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        assert s1 is s2

    def test_sheet_loaded_only_once_for_cached_strip(self, mgr, sheet_path):
        mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        assert _PG.image.load.call_count == 1

    def test_different_rows_produce_different_strips(self, mgr, tmp_path):
        path = str(tmp_path / "tall.png")
        _PG.image._loaded[path] = _PG.Surface((48, 96))
        s0 = mgr.get_strip(path, frame_w=48, frame_h=48, row=0, frame_count=1)
        s1 = mgr.get_strip(path, frame_w=48, frame_h=48, row=1, frame_count=1)
        assert s0 is not s1

    def test_different_frame_dims_produce_different_strips(self, mgr, sheet_path):
        s1 = mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=1)
        s2 = mgr.get_strip(sheet_path, frame_w=32, frame_h=32, row=0, frame_count=1)
        assert s1 is not s2

    def test_scale_resizes_frames(self, mgr, sheet_path):
        frames = mgr.get_strip(
            sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3, scale=(32, 32)
        )
        for f in frames:
            assert f.get_size() == (32, 32)

    def test_transform_scale_called_for_each_frame(self, mgr, sheet_path):
        mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3, scale=(32, 32))
        assert _PG.transform.scale.call_count == 3

    def test_no_scale_skips_transform(self, mgr, sheet_path):
        mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        _PG.transform.scale.assert_not_called()

    def test_scale_skipped_when_frame_already_target_size(self, mgr, sheet_path):
        mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=1, scale=(48, 48))
        _PG.transform.scale.assert_not_called()

    def test_frames_are_independent_copies_of_sheet(self, mgr, tmp_path):
        path = str(tmp_path / "sheet.png")
        sheet = _PG.Surface((48, 48))
        sheet.set_at((0, 0), (10, 20, 30, 255))
        _PG.image._loaded[path] = sheet

        frames = mgr.get_strip(path, frame_w=48, frame_h=48, row=0, frame_count=1)
        original = mgr.load_sheet(path).get_at((0, 0))
        frames[0].set_at((0, 0), (123, 45, 67, 255))
        assert mgr.load_sheet(path).get_at((0, 0)) == original

    def test_strip_key_stored_in_cache(self, mgr, sheet_path):
        mgr.get_strip(sheet_path, frame_w=16, frame_h=32, row=2, frame_count=4, scale=(8, 8))
        expected = StripKey(str(Path(sheet_path)), 16, 32, 2, 4, (8, 8))
        assert expected in mgr._strips

    def test_path_str_and_path_obj_share_strip_cache(self, mgr, tmp_path):
        p_str = str(tmp_path / "sheet.png")
        p_obj = tmp_path / "sheet.png"
        s1 = mgr.get_strip(p_str, frame_w=48, frame_h=48, row=0, frame_count=1)
        s2 = mgr.get_strip(p_obj, frame_w=48, frame_h=48, row=0, frame_count=1)
        assert s1 is s2

    def test_large_frame_count(self, mgr, tmp_path):
        path = str(tmp_path / "wide.png")
        _PG.image._loaded[path] = _PG.Surface((48 * 20, 48))
        assert len(mgr.get_strip(path, frame_w=48, frame_h=48, row=0, frame_count=20)) == 20


# ---------------------------------------------------------------------------
# 4. get_action_strips
# ---------------------------------------------------------------------------

FILENAMES = {
    "LEFT":  "ghost_left.png",
    "RIGHT": "ghost_right.png",
    "UP":    "ghost_up.png",
    "DOWN":  "ghost_down.png",
}


class TestGetActionStrips:
    def test_keys_match_filenames_dict(self, mgr, tmp_path):
        result = mgr.get_action_strips(
            tmp_path, frame_w=48, frame_h=48, frame_count=3, filenames=FILENAMES
        )
        assert set(result.keys()) == set(FILENAMES.keys())

    def test_each_strip_is_tuple_of_correct_length(self, mgr, tmp_path):
        result = mgr.get_action_strips(
            tmp_path, frame_w=48, frame_h=48, frame_count=3, filenames=FILENAMES
        )
        for action, strip in result.items():
            assert isinstance(strip, tuple) and len(strip) == 3

    def test_scale_applied_to_all_frames(self, mgr, tmp_path):
        result = mgr.get_action_strips(
            tmp_path, frame_w=48, frame_h=48, frame_count=3,
            scale=(32, 32), filenames=FILENAMES,
        )
        for action, strip in result.items():
            for f in strip:
                assert f.get_size() == (32, 32)

    def test_second_call_hits_cache(self, mgr, tmp_path):
        kw = dict(frame_w=48, frame_h=48, frame_count=3, scale=(32, 32), filenames=FILENAMES)
        a = mgr.get_action_strips(tmp_path, **kw)
        b = mgr.get_action_strips(tmp_path, **kw)
        for action in FILENAMES:
            assert a[action] is b[action]

    def test_image_loaded_once_per_file(self, mgr, tmp_path):
        kw = dict(frame_w=48, frame_h=48, frame_count=3, filenames=FILENAMES)
        mgr.get_action_strips(tmp_path, **kw)
        mgr.get_action_strips(tmp_path, **kw)
        assert _PG.image.load.call_count == len(FILENAMES)

    def test_empty_filenames_returns_empty_dict(self, mgr, tmp_path):
        assert mgr.get_action_strips(
            tmp_path, frame_w=48, frame_h=48, frame_count=3, filenames={}
        ) == {}

    def test_single_action(self, mgr, tmp_path):
        result = mgr.get_action_strips(
            tmp_path, frame_w=48, frame_h=48, frame_count=2, filenames={"IDLE": "idle.png"}
        )
        assert "IDLE" in result and len(result["IDLE"]) == 2

    def test_directory_str_and_path_share_cache(self, mgr, tmp_path):
        kw = dict(frame_w=48, frame_h=48, frame_count=3, filenames=FILENAMES)
        r1 = mgr.get_action_strips(str(tmp_path), **kw)
        r2 = mgr.get_action_strips(tmp_path, **kw)
        for action in FILENAMES:
            assert r1[action] is r2[action]

    def test_always_uses_row_zero(self, mgr, tmp_path):
        seen_rows = []
        original = mgr.get_strip

        def spy(path, *, row, **kw):
            seen_rows.append(row)
            return original(path, row=row, **kw)

        mgr.get_strip = spy
        mgr.get_action_strips(
            tmp_path, frame_w=48, frame_h=48, frame_count=3,
            filenames={"A": "a.png", "B": "b.png"},
        )
        assert all(r == 0 for r in seen_rows)


# ---------------------------------------------------------------------------
# 5. clear()
# ---------------------------------------------------------------------------

class TestClear:
    def test_clears_sheets_cache(self, mgr, sheet_path):
        mgr.load_sheet(sheet_path)
        mgr.clear()
        assert mgr._sheets == {}

    def test_clears_strips_cache(self, mgr, sheet_path):
        mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        mgr.clear()
        assert mgr._strips == {}

    def test_sheet_reloaded_after_clear(self, mgr, sheet_path):
        mgr.load_sheet(sheet_path)
        mgr.clear()
        mgr.load_sheet(sheet_path)
        assert _PG.image.load.call_count == 2

    def test_strip_recomputed_after_clear(self, mgr, sheet_path):
        s1 = mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        mgr.clear()
        s2 = mgr.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        assert s1 is not s2

    def test_clear_is_idempotent(self, mgr):
        mgr.clear()
        mgr.clear()

    def test_clear_does_not_affect_other_manager_instances(self, mgr, sheet_path):
        mgr2 = AssetManager()
        mgr2.load_sheet(sheet_path)
        mgr.clear()
        assert mgr2._sheets


# ---------------------------------------------------------------------------
# 6. StripKey
# ---------------------------------------------------------------------------

class TestStripKey:
    def test_equal_keys(self):
        assert StripKey("a.png", 48, 48, 0, 3, (32, 32)) == StripKey("a.png", 48, 48, 0, 3, (32, 32))

    def test_differ_by_path(self):
        assert StripKey("a.png", 48, 48, 0, 3, None) != StripKey("b.png", 48, 48, 0, 3, None)

    def test_differ_by_frame_w(self):
        assert StripKey("a.png", 48, 48, 0, 3, None) != StripKey("a.png", 32, 48, 0, 3, None)

    def test_differ_by_frame_h(self):
        assert StripKey("a.png", 48, 48, 0, 3, None) != StripKey("a.png", 48, 32, 0, 3, None)

    def test_differ_by_row(self):
        assert StripKey("a.png", 48, 48, 0, 3, None) != StripKey("a.png", 48, 48, 1, 3, None)

    def test_differ_by_frame_count(self):
        assert StripKey("a.png", 48, 48, 0, 3, None) != StripKey("a.png", 48, 48, 0, 4, None)

    def test_differ_by_scale(self):
        assert StripKey("a.png", 48, 48, 0, 3, (32, 32)) != StripKey("a.png", 48, 48, 0, 3, None)

    def test_hashable(self):
        k = StripKey("a.png", 48, 48, 0, 3, (32, 32))
        assert {k: "v"}[k] == "v"

    def test_frozen(self):
        k = StripKey("a.png", 48, 48, 0, 3, None)
        with pytest.raises((AttributeError, TypeError)):
            k.path = "other.png"  # type: ignore[misc]

    def test_hash_deterministic(self):
        k = StripKey("a.png", 48, 48, 0, 3, (32, 32))
        assert hash(k) == hash(k)


# ---------------------------------------------------------------------------
# 7. Cache isolation
# ---------------------------------------------------------------------------

class TestCacheIsolation:
    def test_independent_sheet_caches(self, sheet_path):
        m1, m2 = AssetManager(), AssetManager()
        m1.load_sheet(sheet_path)
        m2.load_sheet(sheet_path)
        assert m1._sheets is not m2._sheets

    def test_independent_strip_caches(self, sheet_path):
        m1, m2 = AssetManager(), AssetManager()
        s1 = m1.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        s2 = m2.get_strip(sheet_path, frame_w=48, frame_h=48, row=0, frame_count=3)
        assert m1._strips is not m2._strips
        assert s1 is not s2
