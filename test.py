
array = [
    [
        "16:00-16:50",
        [
            "Aula C-112",
            "Ingles"
        ],
        [
            "Lab Elect",
            "Optativa",
            "Palma"
        ],
        [
            "Aula C-112",
            "Ingles"
        ],
        [
            "Lab 2",
            "Ing. Economica",
            "Quijano"
        ],
        [
            "Lab 8",
            "Progra",
            "Mex"
        ]
    ],
    [
        "16:50-17:40",
        [
            "Aula C-112",
            "Ingles"
        ],
        [
            "Lab 8",
            "Progra",
            "Mex"
        ],
        [
            "Aula C-112",
            "Ingles"
        ],
        [
            "Lab 2",
            "Ing. Economica",
            "Quijano"
        ],
        [
            "Lab 8",
            "Progra",
            "Mex"
        ]
    ],
    [
        "17:40-18:30",
        [
            "Lab 5",
            "Mate",
            "Yahaira"
        ],
        [
            "Lab 5",
            "Procesos",
            "Roger"
        ],
        [
            "Lab 5",
            "Mate",
            "Yahaira"
        ],
        [
            "Lab 8",
            "Progra",
            "Mex"
        ],
        "null"
    ],
    [
        "18:30-19:20",
        [
            "Lab 5",
            "Mate",
            "Yahaira"
        ],
        [
            "Lab 5",
            "Procesos",
            "Roger"
        ],
        [
            "Aula C-102",
            "Admin del tiempo",
            "Karla"
        ],
        [
            "Lab 8",
            "Progra",
            "Mex"
        ],
        [
            "Lab 5",
            "Procesos",
            "Roger"
        ]
    ],
    [
        "19:20-20:10",
        [
            "Lab Elect",
            "Optativa",
            "Palma"
        ],
        [
            "Aula C-102",
            "Tutorias",
            "Gimer"
        ],
        [
            "Aula C-102",
            "Admin del tiempo",
            "Karla"
        ],
        [
            "Aula C-102",
            "Admin del tiempo",
            "Karla"
        ],
        [
            "Lab 5",
            "Mate",
            "Yahaira"
        ]
    ],
    [
        "20:10-21:00",
        [
            "Lab Elect",
            "Optativa",
            "Palma"
        ],
        "null",
        [
            "Lab 2",
            "Ing. Economica",
            "Quijano"
        ],
        "null",
        [
            "Lab 5",
            "Mate",
            "Yahaira"
        ]
    ]
]

horario = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

for hour in array:
    for major in hour:
        if major == 'null':
            print(True)
        else:
            if type(major) != str:
                for details in major:
                    print (details)            

"""import shutil

try:
    shutil.copy('resources/excel-sample.xlsx', 'uploads/test.xlsx')
except EnvironmentError:
    print('Error')
else:
    print('Exito')"""