# def dependance_installer(deps: dict[str, list[str]]) -> list[str]:
#     resultat = []
#     lala = deps.copy()  # pour ne pas modifier l'original

#     while lala:
#         # packages installables : toutes leurs dépendances sont déjà installées
#         installables = []

#         for pkg, dependances in lala.items():
#             if all(dep in resultat for dep in dependances):
#                 installables.append(pkg)

#         print(installables)
#         # ordre alphabétique obligatoire
#         installables.sort()

#         # on installe le premier
#         pkg_choisi = installables[0]
#         resultat.append(pkg_choisi)
#         del lala[pkg_choisi]

#     return resultat

def dependance_installer(deps: dict[str, list[str]]) -> list[str]:
    resultat = []
    lala = deps.copy()

    while (lala):
        installable = []

        for pck, dep in lala.items():
            if all(d in resultat for d in dep):
                installable.append(pck)
        installable.sort()
        pck_inst = installable[0]
        resultat.append(pck_inst)
        del lala[pck_inst]
    return resultat

print(dependance_installer({"B": [], "A": ["B", "C"], "C": ["B"]}))