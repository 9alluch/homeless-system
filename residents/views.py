from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Resident, Room
from .forms import ResidentForm
from django.core.paginator import Paginator
from django.db.models import Q

def healthz(request):
    return HttpRespnose("OK")


def home(request):
    return render(request, "residents/home.html")

def dashboard(request):
    total_residents = Resident.objects.count()
    men_count = Resident.objects.filter(gender="M").count()
    women_count = Resident.objects.filter(gender="F").count()
    present_count = Resident.objects.filter(status="active").count()
    left_count = Resident.objects.filter(status="left").count()
    hospital_count = Resident.objects.filter(status="hospital").count()

    total_rooms = Room.objects.count()
    occupied_residents = Resident.objects.filter(room__isnull=False).count()
    full_rooms = sum(1 for room in Room.objects.all() if room.is_full)
    available_spaces = sum(
        room.capacity - room.occupancy
        for room in Room.objects.all()
    )

    return render(
        request,
        "residents/dashboard.html",
        {
            "total_residents": total_residents,
            "men_count": men_count,
            "women_count": women_count,
            "present_count": present_count,
            "left_count": left_count,
            "hospital_count": hospital_count,
            "total_rooms": total_rooms,
            "occupied_residents": occupied_residents,
            "full_rooms": full_rooms,
            "available_spaces": available_spaces,
        }
    )    

def resident_list(request):
    residents = Resident.objects.all()

    search = request.GET.get("search", "")
    gender = request.GET.get("gender", "")
    status = request.GET.get("status", "")
    sort = request.GET.get("sort", "id")

    if search:
        residents = residents.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(phone__icontains=search)
            | Q(nationality__icontains=search)
            | Q(room__number__icontains=search)
         )

    if gender:
        residents = residents.filter(gender=gender)

    if status:
        residents = residents.filter(status=status)

    if sort == "id":
        residents = residents.order_by("id")

    elif sort == "-id":
        residents = residents.order_by("-id")

    elif sort == "last_name":
        residents = residents.order_by("last_name", "first_name")

    elif sort == "-last_name":
        residents = residents.order_by("-last_name", "first_name")

    elif sort == "-admission_date":
        residents = residents.order_by("-admission_date")

    elif sort == "admission_date":
        residents = residents.order_by("admission_date")

    elif sort == "gender":
        residents = residents.order_by("gender", "last_name")

    elif sort == "-gender":
        residents = residents.order_by("-gender", "last_name")

    elif sort == "room":
        residents = residents.order_by("room__number", "last_name")

    elif sort == "-room":
        residents = residents.order_by("-room__number", "last_name")    

    paginator = Paginator(residents, 10)
    page_number = request.GET.get("page")
    residents = paginator.get_page(page_number)

    return render(
        request,
        "residents/residents.html",
        {
            "residents": residents,
            "search": search,
            "selected_gender": gender,
            "selected_status": status,
            "sort": sort,
        }
    )

def resident_detail(request, resident_id):
    resident = Resident.objects.get(id=resident_id)

    return render(
        request,
        "residents/resident_detail.html",
        {"resident": resident}
    )    

def resident_edit(request, resident_id):
    resident = Resident.objects.get(id=resident_id)

    if request.method == "POST":
        form = ResidentForm(request.POST, request.FILES, instance=resident)

        if form.is_valid():
            form.save()
            return redirect("resident_detail", resident_id=resident.id)

    else:
        form = ResidentForm(instance=resident)

    return render(
        request,
        "residents/resident_edit.html",
        {"form": form, "resident": resident}
    )

def resident_create(request):

    if request.method == "POST":
        form = ResidentForm(request.POST, request.FILES)

        if form.is_valid():
            resident = form.save()
            return redirect("resident_detail", resident_id=resident.id)

    else:
        form = ResidentForm()

    return render(
        request,
        "residents/resident_create.html",
        {"form": form}
    )    

def resident_delete(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)

    if request.method == "POST":
        resident.delete()
        return redirect("residents_list")

    return render(
        request,
        "residents/resident_confirm_delete.html",
        {"resident": resident}
    )    