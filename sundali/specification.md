#### Спецификация методов api


* Все устройства - таблица\
getAllMachines
    * machine_id
    * machine_name - инвентарное название/автомобильный номер
    * machine_tech_cd - код типа устройства от поставщика 
    * task_type_desc - тип уборки, к которому пригодно устройство
    * readiness_cd - техническое состояние устройства 'OK', 'CRASH'
    * task_status_desc - текущее состояние задания машины 

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
    * machine_id
    * machine_name
    * Latitude
    * Longitude 
    


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
    * point_id
    * point_type ('depot','street')
    * latitude
    * longitude

* Задания
    * task_id
    * machine_id
    * task_type
    * task_status_cd
    
* Устройства
    * machine_id
    * machine_name
    * machine_type
    * readiness 
 
 *
 *