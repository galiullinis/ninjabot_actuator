from db_manager import DBManager
db_manager = DBManager()

class ActuatorService:
    def get_actuators(self):
        actuators_list = []
        actuators, colnames = db_manager.get_actuators()
        for actuator in actuators:
            actuator_dict = {}
            for ind, col in enumerate(colnames):
                actuator_dict[col] = actuator[ind]

            actuators_list.append(actuator_dict)

        return actuators_list
