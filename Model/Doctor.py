from datetime import datetime

import StaticPatterns
from EntryValidation import EntryValidation
from TimeTable import TimeTable
import re
from Persistency import Persistency


class Doctor(Persistency):

    def __init__(self, user=None, specialty=None, workingdays=None, shifts=None, id=None):
        super().__init__()
        self.timetable = None
        self.id = id
        self.user = user
        self.specialty = specialty
        self.workingdays = workingdays
        self.shifts = shifts

    def validate(self):
        return EntryValidation.validateField(self.specialty, StaticPatterns.SPECIALTY_PATTERN)

    def generateAndSaveCalendar(self):
        tt = TimeTable()
        self.timetable = tt.buildTimeTable(self.workingdays, self.shifts)
        self.insertTimeTable(self.timetable, self.id)

    def validateUser(self):
        valid_login = EntryValidation.validateField(self.user.login, StaticPatterns.LOGIN_PATTERN)
        # valid_workingdays = EntryValidation.validateField(self.user.login, StaticPatterns.WORKINGDAYS)
        return valid_login

    def save_new_doctor(self):
        last_id = 0
        if self.user.validate() and self.validate():
            last_id = self.insert_doctor_trans(self)
        self.id = last_id

    def findDoctor(self):
        if self.user.name:
            result_find_doctor = self.researchDoctor(self)
        else:
            raise IndexError('Invalid name')
        return self

    def findDoctorLogin(self, login):
        return self.findDoctorByLogin(login)

    def findDoctorId(self, doctor_id):
        return self.findDoctorByID(doctor_id)

    def findDoctorName(self, name):
        return self.findDoctorByName(name)

    def getallDoctors(self):
        return self.allDoctors()

    def findFreeDate(self, doctor):
        return self.findFreeDateByDoctor(doctor)

    def getFreeSlots(self, dat, doctor_id):
        if dat is None:
            dat = datetime.now()
        result = self.findDateSlots(dat, doctor_id)
        return re.findall(StaticPatterns.slots, result[0][3])

    def removeSlot(self, dat, slot, doctor_id):
        result = self.getFreeSlots(dat, doctor_id)
        for slotx in result:
            if slotx == slot:
                result.remove(slotx)
                break

        return result

    def returnSlot(self, dat, slot, doctor_id):
        result = self.getFreeSlots(dat, doctor_id)
        result.append(slot)

        return result


