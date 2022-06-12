from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Persona, Familiar
import re

# Create your views here.
def Index(request):
    familiar = Familiar.objects.all()
    return render(request, "index.html", {"familiares": familiar})

def FamiliarIdView(request, id):
    familiar = Familiar.objects.get(pk=id)
    return render(request, "familiar_description.html", {"familiar": familiar})

def editFamiliar(request):
    try:
        familiar = Familiar.objects.get(pk=request.POST["familiar.id"])
        persona = Persona.objects.get(pk=request.POST["persona.id"])
        persona.persona = request.POST["persona"]
        persona.documento = request.POST["documento"]
        persona.fecha_nacimiento = request.POST["fecha_nacimiento"].replace("/", "-")
        familiar.tipo_vinculo = request.POST["tipo_vinculo"]
        if re.search(r"[0-9][0-9]-", persona.fecha_nacimiento):
            split_values = persona.fecha_nacimiento.split("-")
            dia = split_values[0]
            mes = split_values[1]
            anio = split_values[2]
            persona.fecha_nacimiento = f"{anio}-{mes}-{dia}"
        familiar.save()
        print(familiar.tipo_vinculo)
        persona.save()
        return HttpResponse("Persona actualizada correctamente. <a href='/'>Volver al Inicio</a>")
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        msg = str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        })
        print(msg)
        return HttpResponse(f"No se pudo actualizar la persona.<a href='/'>Volver al Inicio</a>")

def deleteFamiliar(request, id):
    persona = Persona.objects.get(pk = id)
    familiar = Familiar.objects.get(persona = persona)
    if request.method=="POST":
        persona.delete()
        return HttpResponseRedirect("/")

    return render(request, "familiar_delete.html", {"persona": persona, "familiar": familiar})

def createFamiliar(request):
    try:
        if request.method=="POST":
            new_persona = request.POST["persona"]
            new_documento = request.POST["documento"]
            new_fecha_nacimiento = request.POST["fecha_nacimiento"].replace("/", "-")
            new_tipo_vinculo = request.POST["tipo_vinculo"]
            if re.search(r"^[0-9][0-9]-", new_fecha_nacimiento):
                split_values = new_fecha_nacimiento.split("-")
                dia = split_values[0]
                mes = split_values[1]
                anio = split_values[2]
                new_fecha_nacimiento = f"{anio}-{mes}-{dia}"
            persona = Persona(persona = new_persona, documento = new_documento, fecha_nacimiento = new_fecha_nacimiento)
            persona.save()
            persona = Persona.objects.get(documento = new_documento)
            familiar = Familiar(persona_id= persona.id, tipo_vinculo = new_tipo_vinculo)
            familiar.save()
            return HttpResponseRedirect("/")
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        msg = str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        })
        return HttpResponse(msg)
    

    return render(request, "familiar_create.html")


    

