import json
import os


class Sg:
    settings_data = None
    def __init__(self):
        self.DIV = os.path.join(os.path.dirname('./'), 'settings.json')
        
        
        try:
            with open(self.DIV, 'r') as file:
                self.settings_data = json.loads(file.read())

        except:
            with open(self.DIV, 'w') as file:
                file.write(self.auto_settings())

        
    def auto_settings(self) -> str:
        self.data = json.dumps(
            {
                "Currency": "USD",
                "Language": "English",
                "Theme": "system",
                "system_mode":"",
                "Sort_en":"All Categories",
                "Sort_ar":"\u062c\u0645\u064a\u0639 \u0627\u0644\u062a\u0635\u0646\u064a\u0641\u0627\u062a"
            }, 
            indent=4
        )
        return self.data
    
    


    def update_settings(self, Currency: str = None, Language: str = None, Theme: str = None):
        self.auto = self.read_settings()
        if Currency:
            self.auto['Currency'] = Currency
        if Language:
            self.auto['Language'] = Language
        if Theme:
            self.auto['Theme'] = Theme
        

        with open(self.DIV, 'w') as file:
            file.write(
                json.dumps(
                    self.auto,
                    indent=4
                )
            )

    def read_settings(self) -> dict:
        with open(self.DIV, 'r') as file:
            se = json.loads(file.read())
        return dict(se)
    
    def backup_settings(self):
        with open(self.DIV, 'w') as file:
                file.write(self.auto_settings())
                a = Colors_settings()
                

    
    def system_mode_read(self):
        self.value = self.read_settings()['system_mode']
        return self.value

    def system_mode_write(self, value: str):
        self.value = value
        self.settings_data = self.read_settings()
        self.settings_data["system_mode"] = self.value

        with open(self.DIV, 'w') as file:
            file.write(
                json.dumps(
                    self.settings_data,
                    indent=4
                )
            )

    def sort_read(self):
        self.settings = Sg().read_settings()
        self.language = self.settings["Language"]

        if self.language == "English":
            self.value = self.read_settings()['Sort_en']
            return self.value
        elif self.language == "\u0627\u0644\u0639\u0631\u0628\u064a\u0629":
            self.value = self.read_settings()['Sort_ar']
            return self.value
        
        return ValueError('language is not found')
    

    def sort_write(self, value: str):
        self.value = value
        self.settings_data = self.read_settings()
        self.settings_data["Sort"] = self.value

        with open(self.DIV, 'w') as file:
            file.write(
                json.dumps(
                    self.settings_data,
                    indent=4
                )
            )

        
        
        


class Colors_settings:
    def __init__(self):
        self.DIV = os.path.join(os.path.dirname('./'), 'colors.json')
        self.settings = Sg().read_settings()
        
        
    def read_all(self):
        with open(self.DIV, 'r') as file:
            return  json.loads(file.read())

    def dark_mode(self):
        data = self.read_all()['dark']
        return data
    
    def light_mode(self):
        data = self.read_all()['light']
        return data
        
    
    def colors_mode(self):

        self.settings = Sg().read_settings()
        self.theme = self.settings["Theme"]
        self.system_mode = self.settings["system_mode"]
        if self.theme == "dark" or self.theme == "\u063a\u0627\u0645\u0642":
            return self.dark_mode()
        elif self.theme == "light" or self.theme == "\u0641\u0627\u062a\u062d":
            return self.light_mode()
        else:
            if self.system_mode == 'dark':
                return self.dark_mode()
            elif self.system_mode == 'light':
                return self.light_mode()
            
    
class Currencies_settinegs:
    def __init__(self):
        self.DIV = os.path.join(os.path.dirname('./'), 'currencies.json')
        self.settings = Sg().read_settings()

    def all_data(self) -> json:
        with open(self.DIV, 'r') as file:
            return json.loads(file.read())["currencies"]
    def data_lang_en(self):
        data = self.all_data()
        inputs = []
        for i in data:
            inputs_dect = {}
            inputs_dect["code"] = i["code"]
            inputs_dect["name"] = i["name_en"]
            inputs_dect["symbol"] = i["symbol_en"]
            inputs.append(inputs_dect)

        return inputs
            
    def data_lang_ar(self):
        data = self.all_data()
        inputs = []
        for i in data:
            inputs_dect = {}
            inputs_dect["code"] = i["code"]
            inputs_dect["name"] = i["name_ar"]
            inputs_dect["symbol"] = i["symbol_ar"]
            inputs.append(inputs_dect)

        return inputs
    
    def data(self):
        self.language = self.settings["Language"]
        
        self.data_l = None
        if self.language == "English" or self.language == "الانجليزية":
            self.data_l = self.data_lang_en()
        elif self.language == "Arbic" or self.language == "\u0627\u0644\u0639\u0631\u0628\u064a\u0629":
            self.data_l = self.data_lang_ar()
        
        
        return self.data_l


    def currencies_mode(self):
        self.settings = Sg().read_settings()
        self.currency = self.settings["Currency"]
        
        self.data_mode = self.data()
        
        for i in self.data_mode:
            if i["code"] == self.currency:
                return i

class languages_settings:
    def __init__(self):
        self.DIV = os.path.join(os.path.dirname('./'), 'languages.json')
        self.settings = Sg().read_settings()


    def language_settings(self):
        self.settings = Sg().read_settings()
        self.language = self.settings["Language"]
        return self.language
    
    def data_en(self):
        with open(self.DIV, 'r') as file:
            return json.loads(file.read())["English"]
        
    def data_ar(self):
        with open(self.DIV, 'r') as file:
            return json.loads(file.read())["Arabic"]
    def data_fr(self):
        with open(self.DIV, 'r') as file:
            return json.loads(file.read())["French"]
        
    def langueage_data(self):
        self.language = self.language_settings()
        
        if self.language == "English":
            return self.data_en()
        elif self.language == "\u0627\u0644\u0639\u0631\u0628\u064a\u0629":
            return self.data_ar()
        elif self.language == "French":
            return self.data_fr()

