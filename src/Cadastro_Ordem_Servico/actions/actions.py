# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from dis import dis
import time
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayShirtSize(Action):

    def name(self) -> Text:
        return "action_say_shirt_size"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("A ordem de serviço número 68744 foi aberta. \n"
        + "Um de nossos atendentes irá entrar em contato para agendar a visita de um técnico.")

        dispatcher.utter_message("Foi agendado um atendimento técnico para o dia 31/05/2022 as 14h referente a ordem de serviço 68744")

        dispatcher.utter_message("O status da ordem de serviço 68744 foi alterado para 'Em andamento'")

        dispatcher.utter_message("A ordem de serviço 68744 foi finalizada pelo técnico Wiler Moraes. \n"
        + "SOLUÇÃO: Formatação realizada no local")

        return []

