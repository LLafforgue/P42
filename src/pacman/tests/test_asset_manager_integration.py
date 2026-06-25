"""
Integration tests for AssetManager.

These tests use REAL pygame and REAL PNG files on disk.
Skipped by default — pass --integration to run them:

    pytest --integration

In CI (no display), set env vars first:
    SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy pytest --integration
"""
from __future__ import annotations

from pathlib import Path

import pytest

from pacman.assets.asset_manager import AssetManager
# Skip the entire module cleanly if pygame is not installed.
# Must be done before any other pygame import.
pygame = pytest.importorskip("pygame")


# ---------------------------------------------------------------------------
# Adjust this to your project layout
# ---------------------------------------------------------------------------

ASSETS_DIR = Path(__file__).parent.parent / "assets" / "ghost"
GHOST_FILES = {
    "LEFT":  "ghost_pink_left_sheet.png",
    "RIGHT": "ghost_pink_right_sheet.png",
    "UP":    "ghost_pink_up_sheet.png",
    "DOWN":  "ghost_pink_down_sheet.png",
}
FRAME_W = FRAME_H = FRAME_COUNT = 48, 48, 3
FRAME_W, FRAME_H, FRAME_COUNT = 48, 48, 3
SCALE = (32, 32)


# ---------------------------------------------------------------------------
# Boot pygame ONCE per module (cheap for a headless window)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module", autouse=True)
def pygame_display():
    pygame.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()


def _require(path: Path):
    if not path.exists():
        pytest.skip(f"Asset not found: {path}")


@pytest.fixture()
def mgr():
    return AssetManager()


@pytest.fixture()
def right_path():
    p = ASSETS_DIR / GHOST_FILES["RIGHT"]
    _require(p)
    return p


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestRealLoadSheet:
    def test_loads_without_error(self, mgr, right_path):
        assert mgr.load_sheet(right_path) is not None

    def test_returns_pygame_surface(self, mgr, right_path):
        assert isinstance(mgr.load_sheet(right_path), pygame.Surface)

    def test_sheet_dimensions(self, mgr, right_path):
        w, h = mgr.load_sheet(right_path).get_size()
        assert w >= FRAME_W and h >= FRAME_H

    def test_has_per_pixel_alpha(self, mgr, right_path):
        assert mgr.load_sheet(right_path).get_bitsize() == 32

    def test_second_call_returns_same_object(self, mgr, right_path):
        assert mgr.load_sheet(right_path) is mgr.load_sheet(right_path)


@pytest.mark.integration
class TestRealGetStrip:
    def test_correct_frame_count(self, mgr, right_path):
        frames = mgr.get_strip(right_path, frame_w=FRAME_W, frame_h=FRAME_H,
                               row=0, frame_count=FRAME_COUNT)
        assert len(frames) == FRAME_COUNT

    def test_unscaled_frame_size(self, mgr, right_path):
        frames = mgr.get_strip(right_path, frame_w=FRAME_W, frame_h=FRAME_H,
                               row=0, frame_count=FRAME_COUNT)
        for f in frames:
            assert f.get_size() == (FRAME_W, FRAME_H)

    def test_scaled_frame_size(self, mgr, right_path):
        frames = mgr.get_strip(right_path, frame_w=FRAME_W, frame_h=FRAME_H,
                               row=0, frame_count=FRAME_COUNT, scale=SCALE)
        for f in frames:
            assert f.get_size() == SCALE

    def test_frames_are_pygame_surfaces(self, mgr, right_path):
        frames = mgr.get_strip(right_path, frame_w=FRAME_W, frame_h=FRAME_H,
                               row=0, frame_count=FRAME_COUNT)
        for f in frames:
            assert isinstance(f, pygame.Surface)

    def test_frames_independent_from_source(self, mgr, right_path):
        frames = mgr.get_strip(right_path, frame_w=FRAME_W, frame_h=FRAME_H,
                               row=0, frame_count=FRAME_COUNT)
        original = mgr.load_sheet(right_path).get_at((0, 0))
        frames[0].set_at((0, 0), (123, 45, 67, 255))
        assert mgr.load_sheet(right_path).get_at((0, 0)) == original

    def test_cache_hit_is_same_object(self, mgr, right_path):
        s1 = mgr.get_strip(right_path, frame_w=FRAME_W, frame_h=FRAME_H,
                           row=0, frame_count=FRAME_COUNT)
        s2 = mgr.get_strip(right_path, frame_w=FRAME_W, frame_h=FRAME_H,
                           row=0, frame_count=FRAME_COUNT)
        assert s1 is s2


@pytest.mark.integration
class TestRealGetActionStrips:
    @pytest.fixture(autouse=True)
    def _require_all(self):
        for fn in GHOST_FILES.values():
            _require(ASSETS_DIR / fn)

    def test_all_directions_present(self, mgr):
        result = mgr.get_action_strips(ASSETS_DIR, frame_w=FRAME_W, frame_h=FRAME_H,
                                       frame_count=FRAME_COUNT, scale=SCALE,
                                       filenames=GHOST_FILES)
        assert set(result.keys()) == set(GHOST_FILES.keys())

    def test_frame_count_per_direction(self, mgr):
        result = mgr.get_action_strips(ASSETS_DIR, frame_w=FRAME_W, frame_h=FRAME_H,
                                       frame_count=FRAME_COUNT, scale=SCALE,
                                       filenames=GHOST_FILES)
        for action, strip in result.items():
            assert len(strip) == FRAME_COUNT

    def test_frame_sizes_after_scaling(self, mgr):
        result = mgr.get_action_strips(ASSETS_DIR, frame_w=FRAME_W, frame_h=FRAME_H,
                                       frame_count=FRAME_COUNT, scale=SCALE,
                                       filenames=GHOST_FILES)
        for action, strip in result.items():
            for f in strip:
                assert f.get_size() == SCALE

    def test_cache_hit_on_second_call(self, mgr):
        kw = dict(frame_w=FRAME_W, frame_h=FRAME_H, frame_count=FRAME_COUNT,
                  scale=SCALE, filenames=GHOST_FILES)
        a = mgr.get_action_strips(ASSETS_DIR, **kw)
        b = mgr.get_action_strips(ASSETS_DIR, **kw)
        for action in GHOST_FILES:
            assert a[action] is b[action]

    def test_strips_are_tuples_of_surfaces(self, mgr):
        result = mgr.get_action_strips(ASSETS_DIR, frame_w=FRAME_W, frame_h=FRAME_H,
                                       frame_count=FRAME_COUNT, scale=SCALE,
                                       filenames=GHOST_FILES)
        for action, strip in result.items():
            assert isinstance(strip, tuple)
            for f in strip:
                assert isinstance(f, pygame.Surface)