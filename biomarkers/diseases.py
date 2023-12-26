from django.utils.translation import gettext_lazy as _


RELATED_TO_BLOOD_PRESSURE = (
    (0, "-----"),
    (1, _("arterial hypotension")),
    (2, _("arterial hypertension of the 1st degree")),
    (3, _("arterial hypertension of the 2st degree")),
    (4, _("arterial hypertension of the 3st degree")),
    (5, _("borderline arterial hypertension")),
    (6, _("isolated systolic hypertension")),
)

RELATED_TO_HEART_RATE = (
    (0, "-----"),
    (1, _("bradicardia")),
    (2, _("tachycardia")),
    (3, _("arrhythmia")),
)

RELATED_TO_EATING_DISORDERS = (
    (0, "-----"),
    (1, _("obesity of the 1st degree")),
    (2, _("obesity of the 2st degree")),
    (3, _("obesity of the 3st degree")),
)

SMOKER = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

SEX = (
    ("MALE", _("Male")),
    ("FEMALE", _("Female")),
)

HYPERTENSION_CHOICE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

APPETITE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

DIABETES = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)


ALCOHOL_CONSUMPTION = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

FAMILY_HISTORY_OF_HEPATITIS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

CHRONIC_FATIGUE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

YELLOW_FINGERS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
FATIGUE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

ANXIETY = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
PEER_PRESSURE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

CHRONIC_DISEASE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

ALLERGY = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

WHEEZING = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
COUGHING = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

SHORTNESS_OF_BREATH = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
SWALLOWING_DIFFICULTY = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

CHEST_PAIN = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)


FAMILY_HISTORY_OF_OVERWEIGHT = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
FREQUENCY_OF_CONSUMPTION_OF_VEGETABLES = (
    ("NEVER", _("Never")),
    ("ALWAYS", _("Always")),
    ("SOMETIMES", _("Sometimes")),
)

FREQUENT_CONS_OF_HIGH_CALORIC_FOOD = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

NUMBER_OF_MAIN_MEALS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)


CONSUMPTION_OF_FOOD_BETWEEN_MEALS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
CONSUMPTION_OF_WATER_DAILY = (
    ("<1L", _("<1L")),
    (">2L", _("2L")),
    (">1-2L", _("1L-2L")),
)

CALORIES_CONSUMPTION_MONITORING = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
PHYSICAL_ACTIVITY_FREQUENCY = (
    ("ACT_NONE", _("None")),
    ("ACT_LOW", _("1-2 times per week")),
    ("ACT_MED", _("2-4 times per week")),
    ("ACT_HIGH", _("4-5 times per week")),
)

TIME_USING_TECHNOLOGY_DEVICES = (
    ("USE_LOW", _("0-2 hours")),
    ("USE_MED", _("3-5 hours")),
    ("USE_HIGH", _("more than 5 hours")),
)

ALCHOL_USE_FREQUENCY = (
    ("USE_NONE_ALCH", _("No")),
    ("USE_LOW_ALCH", _("sometimes")),
    ("USE_MED_ALCH", _("frequently")),
    ("USE_HIGH_ALCH", _("always")),
)

TRANSPORTATION_TYPE = (
    ("WALK", _("Walk")),
    ("BIKE", _("Bike")),
    ("AUTOMOBILE", _("Automobile")),
    ("MOTOR_BIKE", _("Motorbike")),
    ("PUBLIC_TRANSPORT", _("Public transport")),
)
HORMANAL_CONTRACEPTIVES = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

IUD_INTRAUTERINE_DEVICE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_SEXUALLY_TRANSMITTED_DISEASES = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_CONDYLOMATOSIS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_CERVICAL_CONDYLOMATOSIS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_VAGINAL_CONDYLOMATOSIS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_VULVO_PERINEAL_CONDYLOMATOSIS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_SYPHILLIS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_PELVIC_INFLAMMATORY_DISEASE = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_GENITAL_HERPES = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_MOLLUSCUM_CONTAGIOSUM = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_AIDS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_HIV = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_HEPATITIS_B = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

STDS_HPV = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

DIX_CANCER = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

DIX_CIN = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

DIX_HPV = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

SCHILLER = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)
HINSELMANN = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

CITOLOGY = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)

HEPATITIS = (
    ("YES", _("Yes")),
    ("NO", _("No")),
)


MEASURING_SYSTEM = ((1, _("Metric")), (2, _("Inch")))

MENOPAUS_VALUE = (
    (1, _("Pre- or peri-menopausal")),
    (2, _("Post-menopausal")),
    (3, _("Surgical menopause")),
)

GENDERS = (
    (1, _("Male")),
    (2, _("Female")),
)
ACTIVITY_LEVEL = (
    (1.2, _("Minimum")),
    (1.375, _("Lower")),
    (1.55, _("Medium")),
    (1.725, _("High")),
    (1.9, _("Very high")),
)

RACE_GROUP = (
    (1, _("Non-Hispanic white")),
    (2, _("Non-Hispanic black")),
    (3, _("Asian/Pacific Islander")),
    (4, _("Native American")),
    (5, _("Hispanic")),
    (6, _("Other/mixed")),
)
GENERIC_YN = (
    (0, _("No")),
    (1, _("Yes")),
)

ALWAYS = "A"
SOMETIMES = "S"
NEVER = "N"
TRIP_ANS = (
    (ALWAYS, _("Always")),
    (SOMETIMES, _("Sometimes")),
    (NEVER, _("Never")),
)


ACT_NONE = "N"
ACT_LOW = "L"
ACT_MED = "M"
ACT_HIGH = "H"
ACTIVITY_WEEK_DAYS = (
    (ACT_NONE, _("None")),
    (ACT_LOW, _("1-2 times per week")),
    (ACT_MED, _("2-4 times per week")),
    (ACT_HIGH, _("4-5 times per week")),
)


USE_LOW = "L"
USE_MED = "M"
USE_HIGH = "H"
TECH_USE_FREQUENCY = (
    (USE_LOW, _("0-2 times per week")),
    (USE_MED, _("3-5 times per week")),
    (USE_HIGH, _("more than 5 times per week")),
)

USE_NONE_ALCH = "N"
USE_LOW_ALCH = "L"
USE_MED_ALCH = "M"
USE_HIGH_ALCH = "H"
ALCHOL_USE_FREQUENCY = (
    (USE_NONE_ALCH, _("None")),
    (USE_LOW_ALCH, _("sometimes")),
    (USE_MED_ALCH, _("frequently")),
    (USE_HIGH_ALCH, _("always")),
)

WALK = "W"
BIKE = "B"
AUTOMOBILE = "A"
MOTOR_BIKE = "M"
PUBLIC_TRANSPORT = "P"
