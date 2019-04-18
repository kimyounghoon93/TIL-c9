from django.db import models

# Create your models here.
# 병원에 오는 사람들을 기록하는 시스템을 만드려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있을까?

class Doctor(models.Model):
    name = models.TextField()
    
# 1 대 N 관계
class Patient(models.Model):
    name = models.TextField()               # 편리한 용어를 위하여 related_name='patients'
                                            # 의사가 환자를 불러올 때 사용될 언어를 지정해줌
    doctors = models.ManyToManyField(Doctor, related_name='patients') # through='Reservation'
    
# Doctor:Reservation = 1:N -> Reservation = N*Doctor
# Patient:Reservation = 1:N -> Reservation = M*Paatient
# N*Doctor = M*Patient -> M:N = Doctor:Patient
# Doctor:Patient = M:N
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
# 의사 2명 환자 2명 만들기
# doctor1 = Doctor.objects.create(name='kim')
# doctor2 = Doctor.objects.create(name='kang')                                                    
# patient1 = Patient.objects.create(name='tom')
# patient2 = Patient.objects.create(name='john')
# Reservation.object.create(dotor=doctor1, patient=patient2)
# Reservation.objects.create(doctor=doctor1, patient=patient2)
# doctor1.reservation_set.all()
# patient2.reservation_set.all()
# Reservation.objects.create(doctor=doctor1, patient=patient1)

# 1번 의사의 모든 예약들을 가져온다
# doctor1.reservation_set.all()

# 환자의 정보, 리스트를 보기
#for res in doctor1.reservation_set.all():
# ...     print(res.patient.name)

# 의사가 환자 정보로 바로가기 혹은 환자가 의사정보로 바로가기
# class Patient(models.Model):
#    name = models.TextField()
# 추가    doctors = models.ManyToManyField(Doctor, through='Reservation')
# doctor1 = Doctor.objects.get(pk=1)
# doctor1
# patient1 = Patient.objects.get(pk=1)
# patient1
# patient1.doctors.all()

# >>> doctor1 = Doctor.objects.create(name='Kim')
# >>> doctor2 = Doctor.objects.create(name='Kang')                                                    
# >>> patient1 = Patient.objects.create(name='Tom')
# >>> patient2 = Patient.objects.create(name='John')
#doctor1.patients.all()
# # <QuerySet []>

# >>> patient2.doctors.all()
# <QuerySet []>
# doctor1.patients.add(patient2)
# >>> doctor1.patients.all()
# <QuerySet [<Patient: Patient object (2)>]>
# >>> patient2.doctors.all()
# <QuerySet [<Doctor: Doctor object (1)>]>

# # 삭제
# doctor1.patients.remove(patient2)