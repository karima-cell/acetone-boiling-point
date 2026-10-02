import numpy as np
import matplotlib.pyplot as plt

# ============================================================
#             ETUDE DE L'EBULLITION DE L'ACETONE
# ============================================================

# ------------------------------------------------------------
# 1. DONNEES DU PROBLEME
# ------------------------------------------------------------

m_total = 38.0          # débit total d'acétone [kg/h]
fraction_F2 = 0.60      # 60 % vers le Heater

m_F2 = m_total * fraction_F2

T_entree_C = 10.0      # température d'entrée [°C]
P_reference_atm = 1.0  # pression de référence [atm]

# Propriétés de l'acétone
Cp = 2.15              # chaleur massique liquide [kJ/(kg.K)]
Hvap = 500.0           # chaleur latente [kJ/kg]
M = 58.08              # masse molaire [g/mol]

# ------------------------------------------------------------
# 2. CONSTANTES D'ANTOINE POUR L'ACETONE
#    log10(P) = A - B/(T+C)
#    P en bar ; T en K
# ------------------------------------------------------------

A = 4.42448
B = 1312.253
C = -32.445


# ------------------------------------------------------------
# 3. FONCTION : TEMPERATURE D'EBULLITION
# ------------------------------------------------------------

def temperature_ebullition(P_atm):

    # Conversion atm -> bar
    P_bar = P_atm * 1.01325

    # Equation d'Antoine
    T_K = B / (A - np.log10(P_bar)) - C

    # Conversion K -> °C
    T_C = T_K - 273.15

    return T_K, T_C


# ============================================================
#                    PARTIE 1
#          CALCUL A 60 % ET A 1 ATM
# ============================================================

print("\n")
print("=" * 65)
print("          ETUDE DE L'EBULLITION DE L'ACETONE")
print("=" * 65)

print("\n[1] DONNEES DU PROBLEME")
print("-" * 65)

print(f"Débit total d'acétone       : {m_total:.2f} kg/h")
print(f"Fraction envoyée au Heater  : {fraction_F2*100:.0f} %")

print(f"Débit F2 vers le Heater     : {m_F2:.2f} kg/h")

print(f"Température d'entrée        : {T_entree_C:.2f} °C")
print(f"Pression                    : {P_reference_atm:.2f} atm")


# ------------------------------------------------------------
# Temperature d'ébullition à 1 atm
# ------------------------------------------------------------

T_eb_K, T_eb_C = temperature_ebullition(P_reference_atm)

print("\n")
print("=" * 65)
print("       2. TEMPERATURE D'EBULLITION A 1 ATM")
print("=" * 65)

print(f"\nPression                    : {P_reference_atm:.2f} atm")
print(f"Pression                    : {P_reference_atm*1.01325:.5f} bar")

print(f"\nTempérature d'ébullition    : {T_eb_K:.2f} K")
print(f"Température d'ébullition    : {T_eb_C:.2f} °C")


# ============================================================
#                    PARTIE 2
#                 CALCUL DE L'ENERGIE
# ============================================================

print("\n")
print("=" * 65)
print("              3. ENERGIE DU HEATER")
print("=" * 65)

# ------------------------------------------------------------
# A. Chauffage du liquide
# ------------------------------------------------------------

DeltaT = T_eb_C - T_entree_C

Q_sensible_kJh = m_F2 * Cp * DeltaT

Q_sensible_kW = Q_sensible_kJh / 3600


# ------------------------------------------------------------
# B. Vaporisation
# ------------------------------------------------------------

Q_vaporisation_kJh = m_F2 * Hvap

Q_vaporisation_kW = Q_vaporisation_kJh / 3600


# ------------------------------------------------------------
# C. Energie totale
# ------------------------------------------------------------

Q_total_kJh = Q_sensible_kJh + Q_vaporisation_kJh

Q_total_kW = Q_total_kJh / 3600


print("\n--- Chauffage du liquide ---")

print(f"ΔT                         : {DeltaT:.2f} K")

print(f"Q sensible                 : {Q_sensible_kJh:.2f} kJ/h")
print(f"Q sensible                 : {Q_sensible_kW:.3f} kW")


print("\n--- Vaporisation ---")

print(f"Q vaporisation             : {Q_vaporisation_kJh:.2f} kJ/h")
print(f"Q vaporisation             : {Q_vaporisation_kW:.3f} kW")


print("\n--- ENERGIE TOTALE ---")

print(f"Q total                    : {Q_total_kJh:.2f} kJ/h")
print(f"Q total                    : {Q_total_kW:.3f} kW")


# ============================================================
#                    PARTIE 3
#       ETUDE DE SENSIBILITE : 0.1 -> 3 atm
# ============================================================

print("\n")
print("=" * 65)
print("       4. ETUDE DE SENSIBILITE : T_eb = f(P)")
print("=" * 65)

P_min = 0.1
P_max = 3.0
N = 25

# Création des 25 pressions
P_atm = np.linspace(P_min, P_max, N)

# Calcul des températures
T_eb_K_values = []
T_eb_C_values = []

for P in P_atm:

    TK, TC = temperature_ebullition(P)

    T_eb_K_values.append(TK)
    T_eb_C_values.append(TC)


# ============================================================
#                     TABLEAU RESULTATS
# ============================================================

print("\n")
print("  N°       P (atm)       T_eb (K)       T_eb (°C)")
print("-" * 65)

for i in range(N):

    print(
        f"{i+1:3d}"
        f"{P_atm[i]:15.4f}"
        f"{T_eb_K_values[i]:15.2f}"
        f"{T_eb_C_values[i]:15.2f}"
    )


# ============================================================
#                     GRAPHE
# ============================================================

plt.figure(figsize=(9, 6))

plt.plot(
    P_atm,
    T_eb_C_values,
    marker='o',
    linewidth=2
)

plt.xlabel("Pression (atm)")
plt.ylabel("Température d'ébullition (°C)")

plt.title(
    "Variation de la température d'ébullition de l'acétone\n"
    "en fonction de la pression"
)

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
#                       FIN
# ============================================================

print("\n")
print("=" * 65)
print("                    FIN DU CALCUL")
print("=" * 65)

print(f"\nDébit chauffé F2           = {m_F2:.2f} kg/h")
print(f"T ébullition à 1 atm       = {T_eb_C:.2f} °C")
print(f"Energie totale à 1 atm     = {Q_total_kW:.3f} kW")

print("\nLa courbe T_eb = f(P) a été tracée avec 25 points.")
print("=" * 65)
