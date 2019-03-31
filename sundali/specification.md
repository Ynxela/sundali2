#### Спецификация методов api


* Все устройства - таблица\
getAllMachines
    * machine_id
    * machine_name - инвентарное название/автомобильный номер
    * machine_tech_cd - код типа устройства от поставщика 
    * task_type_cd - тип уборки, к которому пригодно устройство
    * readiness_cd - техническое состояние устройства 'OK', 'CRASH'
    * task_status_cd - текущее состояние задания машины 

* Текущие задания\
getCurrentTasks \
Возвращает задания, которые находятся в активных статусах

* Все задания\
getAllTasks\
Возвращает все задания

* Нотификации\
getNewMessages\
Возвращает нотификации в статусе не прочитано
 

* Текущая локация устройств\
getMachinesLocation 
    * depot_latitude
    * depot_longitude
        * machine_id
        * machine_name
        * task_type_cd
        * task_status_cd
        * Latitude
        * Longitude
        
JSON getMachinesLocation

coordinates: [55.7963846, 37.536643],
markers: [
  {
    coordinates: [55.8072856, 37.536643],
    machine_name: 'Car 1',
    task_status_cd: 'FAIL',
    machine_id: 1,
    task_type_cd: 0,
  },
  {
    coordinates: [55.8072856, 37.536643],
    machine_name: 'Car 2',
    task_status_cd: 'IN_PROGRESS',
    machine_id: 2,
    task_type_cd: 0,
  },
  {
    coordinates: [55.8072856, 37.536643],
    machine_name: 'Car 3',
    task_status_cd: 'IN_PROGRESS',
    machine_id: 3,
    task_type_cd: 0,
  },
],       


* Расположение депо\
getDepotLocation\
Возвращает координаты депо, необходим для первоначальной локации карты




#### Описание структуры данных

##### Сущности
* Основной граф
* Устройства
    * История телеметрии 
* Задания
    * Марштут задания
* Информация с погодных датчиков
* Нотификации
* Депо

##### Детализация сущностей
* Основной граф
    * point_id (pk)
    * point_type ('DEPOT','LOCATION')
    * latitude
    * longitude

* Задания
    * task_id (pk)
    * machine_id (fk)
    * task_type_cd
    * task_status_cd

* Точки задания
    * task_id (pk)
    * point_id (pk)
    * latitude
    * longitude    
   
* Устройства
    * machine_id (pk)
    * machine_name
    * machine_type_cd
    * readiness 
 
 *
 
 *