import json
from django.http import JsonResponse
from django.views import View
from .models import Task
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class TareaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            companies = list(Task.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {"mensaje": "exito", "company": company}
            else:
                datos = {"mensaje": "tarea no encontrada"}
            return JsonResponse(datos)
        else:
            tareas = Task.objects.all()
            if len(tareas) > 0:
                datos = {"mensaje": "success", "tareas": list(tareas.values())}
            else:
                datos = {"mensaje": "tareas no encontradas"}
            return JsonResponse(datos)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            # Accede a los datos del JSON correctamente usando la variable jd
            Task.objects.create(titulo=jd.get('title'), descripcion=jd.get('des'))
            datos = {"mensaje": "realizado con exito"}
            return JsonResponse(datos)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def put(self, request, id):
    	jd = json.loads(request.body)
    	companies = list(Task.objects.filter(id=id).values())
    	if len(companies) > 0:
    		task = Task.objects.get(id=id)
    		task.titulo = jd.get('title')
    		task.descripcion = jd.get('des')
    		task.save()
    		return JsonResponse({"mensaje": "editado con exito"})
    	else:
    		return JsonResponse({"mensaje": "no se encontro la tarea"}, status=404)

    def delete(self, request, id):
    	Task.objects.filter(id=id).delete()
    	return JsonResponse({"mensaje": "eliminado con exito"})