# main.py
# -*- coding: utf-8 -*-
"""
Módulo de apoyo para operaciones sobre:
    • Cadenas (strings)
    • Lenguajes (conjuntos de cadenas)
    • Autómatas finitos (AFD que reconoce exactamente un lenguaje finito L)

Todas las funciones son estáticas para que puedan invocarse sin instanciar la clase.
"""

from itertools import product, islice
from typing import Iterable, List, Set, Dict, Tuple


class Main:
    # ========== AUXILIARES =================================================

    @staticmethod
    def _potencia_str(s: str, n: int) -> str:
        """Devuelve s^n (n ≥ 0)."""
        if n < 0:
            raise ValueError("La potencia debe ser no negativa")
        return s * n

    @staticmethod
    def _potencia_lenguaje(L: Set[str], n: int) -> Set[str]:
        """
        Potencia n-ésima de un lenguaje:
            L⁰ = {ε}
            Lⁿ = { w1 … wn | wi ∈ L }
        """
        if n < 0:
            raise ValueError("La potencia debe ser no negativa")

        if n == 0:
            return {""}

        resultado = set([""])
        for _ in range(n):
            resultado = {x + y for x in resultado for y in L}
        return resultado

    # ========== OPERACIONES CON CADENAS ====================================

    @staticmethod
    def concatenacion_cadena(w: str, x: str) -> str:
        """Concatenación de cadenas: w ∘ x."""
        return w + x

    @staticmethod
    def potencia_cadena(w: str, n: int, x: str, m: int) -> Dict[str, str]:
        """
        Potencias de cadenas.
        Devuelve un diccionario con w^n y x^m.
        """
        return {
            "w^n": Main._potencia_str(w, n),
            "x^m": Main._potencia_str(x, m),
        }

    @staticmethod
    def inversa_cadena(w: str, x: str) -> Dict[str, str]:
        """Inversa (reversa) de cada cadena."""
        return {"wʳ": w[::-1], "xʳ": x[::-1]}

    @staticmethod
    def longitud_cadena(w: str, x: str) -> Dict[str, int]:
        """Longitud |w| y |x|."""
        return {"|w|": len(w), "|x|": len(x)}

    @staticmethod
    def comparacion_cadenas(w: str, x: str) -> bool:
        """True si w == x."""
        return w == x

    @staticmethod
    def prefijos_sufijos(w: str, x: str) -> Dict[str, Dict[str, List[str]]]:
        """Devuelve todos los prefijos y sufijos de w y de x."""
        def prefijos(s: str) -> List[str]:
            return [s[:i] for i in range(len(s) + 1)]

        def sufijos(s: str) -> List[str]:
            return [s[i:] for i in range(len(s) + 1)]

        return {
            "w": {"prefijos": prefijos(w), "sufijos": sufijos(w)},
            "x": {"prefijos": prefijos(x), "sufijos": sufijos(x)},
        }

    @staticmethod
    def union_cadenas(w: str, x: str) -> Set[str]:
        """
        Unión de caracteres de w y x (pensando en w, x ⊆ Σ* con |w| = |x| = 1).
        Si las cadenas tienen varios símbolos devolverá la unión de sus alfabetos.
        """
        return set(w) | set(x)

    @staticmethod
    def clausula_kleene_cadena(
        w: str, x: str, max_power: int = 3
    ) -> Dict[str, Set[str]]:
        """
        Aproximación finita de la clausura de Kleene:
        devuelva {ε, s, s², …, s^k} para k = max_power.
        """
        return {
            "w*": {Main._potencia_str(w, i) for i in range(max_power + 1)},
            "x*": {Main._potencia_str(x, i) for i in range(max_power + 1)},
        }

    @staticmethod
    def clausula_positiva_cadena(
        w: str, x: str, max_power: int = 3
    ) -> Dict[str, Set[str]]:
        """Cláusula positiva (sin ε)."""
        return {
            "w⁺": {Main._potencia_str(w, i) for i in range(1, max_power + 1)},
            "x⁺": {Main._potencia_str(x, i) for i in range(1, max_power + 1)},
        }

    # ========== OPERACIONES CON LENGUAJES ==================================

    @staticmethod
    def concatenacion_lenguaje(L1: Iterable[str], L2: Iterable[str]) -> Set[str]:
        """L1 ∘ L2 = { u v | u∈L1, v∈L2 }."""
        return {u + v for u, v in product(L1, L2)}

    @staticmethod
    def union_lenguaje(L1: Iterable[str], L2: Iterable[str]) -> Set[str]:
        """L1 ∪ L2."""
        return set(L1) | set(L2)

    @staticmethod
    def interseccion_lenguaje(L1: Iterable[str], L2: Iterable[str]) -> Set[str]:
        """L1 ∩ L2."""
        return set(L1) & set(L2)

    @staticmethod
    def diferencia_lenguaje(L1: Iterable[str], L2: Iterable[str]) -> Dict[str, Set[str]]:
        """Devuelve ambas diferencias: L1−L2 y L2−L1."""
        return {
            "L1−L2": set(L1) - set(L2),
            "L2−L1": set(L2) - set(L1),
        }

    @staticmethod
    def potencia_lenguaje(L: Iterable[str], n: int) -> Set[str]:
        """L^n (usa la ayuda privada)."""
        return Main._potencia_lenguaje(set(L), n)

    @staticmethod
    def inversa_lenguaje(L: Iterable[str]) -> Set[str]:
        """Lʳ = { wʳ | w ∈ L }."""
        return {w[::-1] for w in L}

    @staticmethod
    def clausula_kleene_lenguaje(L: Iterable[str], max_power: int = 3) -> Set[str]:
        """L* aproximado hasta max_power."""
        conjunto = set([""])  # ε
        for k in range(1, max_power + 1):
            conjunto |= Main._potencia_lenguaje(set(L), k)
        return conjunto

    @staticmethod
    def clausula_positiva_lenguaje(L: Iterable[str], max_power: int = 3) -> Set[str]:
        """L⁺ aproximado (sin ε)."""
        conjunto = set()
        for k in range(1, max_power + 1):
            conjunto |= Main._potencia_lenguaje(set(L), k)
        return conjunto

    # ========== AUTÓMATA FINITO (AFD) ======================================

    @staticmethod
    def automata_finito(L: Iterable[str]) -> Dict[str, object]:
        """
        Construye un AFD que reconoce *exactamente* el lenguaje finito L
        mediante un trie (árbol de prefijos). Devuelve una
        representación serializable con:
            • states:     lista de estados
            • alphabet:   conjunto de símbolos
            • initial:    estado inicial
            • finals:     lista de estados finales
            • transitions:{estado: {símbolo: estado_destino}}
        """
        # Construcción del trie
        estado_actual = 0
        contador = 1
        trans: Dict[int, Dict[str, int]] = {}
        finales: Set[int] = set()
        alphabet: Set[str] = set()

        for palabra in L:
            estado = 0  # raíz
            for simbolo in palabra:
                alphabet.add(simbolo)
                if estado not in trans:
                    trans[estado] = {}
                if simbolo not in trans[estado]:
                    trans[estado][simbolo] = contador
                    estado = contador
                    contador += 1
                else:
                    estado = trans[estado][simbolo]
            finales.add(estado)

        estados = list(range(contador))

        return {
            "states": estados,
            "alphabet": sorted(alphabet),
            "initial": 0,
            "finals": sorted(finales),
            "transitions": trans,
        }
