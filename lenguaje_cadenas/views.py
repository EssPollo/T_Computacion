# views.py
# -*- coding: utf-8 -*-

from rest_framework import status, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .main import Main


# ────────────────────
# Serializers de entrada
# ────────────────────
class DosCadenasSerializer(serializers.Serializer):
    w = serializers.CharField(help_text="Primera cadena")
    x = serializers.CharField(help_text="Segunda cadena")


class PotenciaCadenasSerializer(serializers.Serializer):
    w = serializers.CharField()
    x = serializers.CharField()
    n = serializers.IntegerField(min_value=0, help_text="Exponente para w")
    m = serializers.IntegerField(min_value=0, help_text="Exponente para x")


class UnNumeroCadenaSerializer(serializers.Serializer):
    w = serializers.CharField()
    n = serializers.IntegerField(min_value=0, default=1)


class DosLenguajesSerializer(serializers.Serializer):
    L1 = serializers.ListField(
        child=serializers.CharField(), help_text="Primer lenguaje (lista de cadenas)"
    )
    L2 = serializers.ListField(
        child=serializers.CharField(), help_text="Segundo lenguaje"
    )


class UnLenguajeSerializer(serializers.Serializer):
    L1 = serializers.ListField(child=serializers.CharField())


class PotenciaLenguajeSerializer(serializers.Serializer):
    L1 = serializers.ListField(child=serializers.CharField())
    n = serializers.IntegerField(min_value=0)


# ────────────────────
# ViewSet principal
# ────────────────────
class OperacionesViewSet(viewsets.ViewSet):
    """
    API para operaciones sobre Cadenas, Lenguajes y Autómatas Finitos.
    Cada acción valida estrictamente su entrada y devuelve un JSON:
    """

    # ========== CADENAS ===================================================

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="1 · Concatenación de cadenas",
        request_body=DosCadenasSerializer,
        responses={200: "Cadena concatenada", 400: "Solicitud mal formada"},
    )
    def concatenacion_cadenas(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.concatenacion_cadena(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="2 · Potencia de cadenas",
        request_body=PotenciaCadenasSerializer,
        responses={200: "Diccionario con w^n y x^m"},
    )
    def potencia_cadenas(self, request):
        s = PotenciaCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.potencia_cadena(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="3 · Inversa de una cadena",
        request_body=DosCadenasSerializer,
        responses={200: "Diccionario con wʳ y xʳ"},
    )
    def inversa_cadena(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.inversa_cadena(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="4 · Longitud de una cadena",
        request_body=DosCadenasSerializer,
        responses={200: "Diccionario con |w| y |x|"},
    )
    def longitud_cadena(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.longitud_cadena(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="5 · Comparación de cadenas",
        request_body=DosCadenasSerializer,
        responses={200: "true / false"},
    )
    def comparacion_cadenas(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.comparacion_cadenas(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="6 · Prefijos y Sufijos",
        request_body=DosCadenasSerializer,
        responses={200: "Diccionario con prefijos y sufijos de w y x"},
    )
    def prefijos_sufijos(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.prefijos_sufijos(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="7 · Unión de cadenas (alfabetos)",
        request_body=DosCadenasSerializer,
        responses={200: "Conjunto unión"},
    )
    def union_cadenas(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.union_cadenas(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="8 · Cláusula de Kleene de una cadena",
        request_body=DosCadenasSerializer,
        responses={200: "Diccionario con w* y x*"},
    )
    def clausula_kleene_cadena(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.clausula_kleene_cadena(**s.validated_data)
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="9 · Cláusula Positiva de una cadena",
        request_body=DosCadenasSerializer,
        responses={200: "Diccionario con w⁺ y x⁺"},
    )
    def clausula_positiva_cadena(self, request):
        s = DosCadenasSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.clausula_positiva_cadena(**s.validated_data)
        return Response({"resultado": res})

    # ========== LENGUAJES ==================================================

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="10 · Concatenación de lenguajes",
        request_body=DosLenguajesSerializer,
        responses={200: "L1 ∘ L2"},
    )
    def concatenacion_lenguajes(self, request):
        s = DosLenguajesSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.concatenacion_lenguaje(**s.validated_data)
        return Response({"resultado": list(res)})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="11 · Unión de lenguajes",
        request_body=DosLenguajesSerializer,
        responses={200: "L1 ∪ L2"},
    )
    def union_lenguajes(self, request):
        s = DosLenguajesSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.union_lenguaje(**s.validated_data)
        return Response({"resultado": list(res)})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="12 · Intersección de lenguajes",
        request_body=DosLenguajesSerializer,
        responses={200: "L1 ∩ L2"},
    )
    def interseccion_lenguajes(self, request):
        s = DosLenguajesSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.interseccion_lenguaje(**s.validated_data)
        return Response({"resultado": list(res)})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="13 · Diferencia de lenguajes",
        request_body=DosLenguajesSerializer,
        responses={200: "{L1−L2, L2−L1}"},
    )
    def diferencia_lenguajes(self, request):
        s = DosLenguajesSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        res = Main.diferencia_lenguaje(**s.validated_data)
        # sets → lists para serializar
        res = {k: list(v) for k, v in res.items()}
        return Response({"resultado": res})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="14 · Potencia de un lenguaje",
        request_body=PotenciaLenguajeSerializer,
        responses={200: "L^n"},
    )
    def potencia_lenguaje(self, request):
        s = PotenciaLenguajeSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        L = s.validated_data["L1"]
        n = s.validated_data["n"]
        res = Main.potencia_lenguaje(L, n)
        return Response({"resultado": list(res)})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="15 · Inversa de un lenguaje",
        request_body=UnLenguajeSerializer,
        responses={200: "Lʳ"},
    )
    def inversa_lenguaje(self, request):
        s = UnLenguajeSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        L = s.validated_data["L1"]
        res = Main.inversa_lenguaje(L)
        return Response({"resultado": list(res)})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="16 · Cláusula de Kleene de un lenguaje",
        request_body=UnLenguajeSerializer,
        responses={200: "L* (hasta potencia k)"},
    )
    def clausula_kleene_lenguaje(self, request):
        s = UnLenguajeSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        L = s.validated_data["L1"]
        res = Main.clausula_kleene_lenguaje(L)
        return Response({"resultado": list(res)})

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="17 · Cláusula Positiva de un lenguaje",
        request_body=UnLenguajeSerializer,
        responses={200: "L⁺ (hasta potencia k)"},
    )
    def clausula_positiva_lenguaje(self, request):
        s = UnLenguajeSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        L = s.validated_data["L1"]
        res = Main.clausula_positiva_lenguaje(L)
        return Response({"resultado": list(res)})

    # ========== AUTÓMATAS ==================================================

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_summary="18 · Autómata Finito a partir de un lenguaje",
        request_body=UnLenguajeSerializer,
        responses={200: "AFD como diccionario"},
    )
    def automata_finito(self, request):
        s = UnLenguajeSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        L = s.validated_data["L1"]
        res = Main.automata_finito(L)
        return Response({"resultado": res})