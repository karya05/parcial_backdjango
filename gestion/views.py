
import json
from django.http import JsonResponse
from django.views import View
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Project


@method_decorator(csrf_exempt, name='dispatch')
class ProjectEndpoint(View):

    def get(self, request, pk=None):
        if pk is None:
            proyectos = list(Project.objects.values())
            return JsonResponse(proyectos, safe=False)

        try:
            proyecto = Project.objects.get(pk=pk)
            datos = {
                "id": proyecto.id,
                "name": proyecto.name,
                "description": proyecto.description,
                "start_date": str(proyecto.start_date)
            }
            return JsonResponse(datos)
        except Project.DoesNotExist:
            return JsonResponse({"error": "Proyecto no encontrado"}, status=404)

    def post(self, request):
        try:
            datos = json.loads(request.body)
            fecha = parse_date(datos.get("start_date", ""))

            if not datos.get("name") or not datos.get("description") or not fecha:
                return JsonResponse(
                    {"error": "Envía name, description y start_date (AAAA-MM-DD)"},
                    status=400
                )

            proyecto = Project.objects.create(
                name=datos["name"],
                description=datos["description"],
                start_date=fecha
            )

            return JsonResponse(
                {"mensaje": "Proyecto creado", "id": proyecto.id},
                status=201
            )
        except (json.JSONDecodeError, TypeError):
            return JsonResponse({"error": "JSON no válido"}, status=400)

    def put(self, request, pk=None):
        if pk is None:
            return JsonResponse({"error": "Debes indicar el ID del proyecto"}, status=400)

        try:
            proyecto = Project.objects.get(pk=pk)
            datos = json.loads(request.body)

            if "name" in datos:
                proyecto.name = datos["name"]

            if "description" in datos:
                proyecto.description = datos["description"]

            if "start_date" in datos:
                fecha = parse_date(datos["start_date"])
                if not fecha:
                    return JsonResponse({"error": "Fecha no válida"}, status=400)
                proyecto.start_date = fecha

            proyecto.save()
            return JsonResponse({"mensaje": "Proyecto actualizado"})
        except Project.DoesNotExist:
            return JsonResponse({"error": "Proyecto no encontrado"}, status=404)
        except (json.JSONDecodeError, TypeError):
            return JsonResponse({"error": "JSON no válido"}, status=400)

    def delete(self, request, pk=None):
        if pk is None:
            return JsonResponse({"error": "Debes indicar el ID del proyecto"}, status=400)

        try:
            proyecto = Project.objects.get(pk=pk)
            proyecto.delete()
            return JsonResponse({"mensaje": "Proyecto eliminado"})
        except Project.DoesNotExist:
            return JsonResponse({"error": "Proyecto no encontrado"}, status=404)
        
