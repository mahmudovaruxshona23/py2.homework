class Phone():
    def __init__(self, versiya, q_name, story, p_model, ram):
        self.versiya = versiya
        self.q_name = q_name
        self.story = story
        self.p_model = p_model
        self.ram = ram

    def get_versiya(self):
        return self.versiya
    def get_q_name(self):
        return self.q_name
    def get_story(self):
        return self.story
    def get_p_model(self):
        return self.p_model
    def get_ram(self):
        return self.ram
    
    def set_versiya(self, new_versiya):
        self.versiya = new_versiya
    def set_q_name(self, new_q_name):
        self.q_name = new_q_name
    def set_story(self, new_story):
        self.story = new_story
    def set_p_model(self, new_p_model):
        self.p_model = new_p_model
    def set_ram(self,new_ram):
        self.ram = new_ram

    def info(self):
        info = f"versiyasi: {self.versiya}. q_name: {self.q_name}. story: {self.story}. p_model: {self.p_model}. ram: {self.ram}"
        return info



p = Phone('MIUI', 'Arsenal', '76GB', 'Redmi12', '5,00GB')

print(p.info())

class M_Phone(Phone):
    def __init__(self, versiya, q_name, story, p_model, ram, CPU, applications):
        super().__init__(versiya, q_name, story, p_model, ram)
        self.CPU = CPU
        self.applications = applications
        

    def info(self):
        info = f"versiyasi: {self.versiya}. q_name: {self.q_name}. story: {self.story}. p_model: {self.p_model}. ram: {self.ram}. CPU: {self.CPU}"
        return info
    
class Applications():
    def __init__(self , sms, text, vidio, films):
        self.sms = sms
        self.text = text
        self.vidio = vidio
        self.films = films
        
    def info(self):
        info = f"{self.sms}: sms, {self.text}: text, {self.vidio}: vidios, {self.films}: films"
        return info

applications = Applications("Messenge", "Telegram", "XPlayer", "You tube")



n = M_Phone("MIUI", 'Arsenal', '76GB', 'Redmi12', '5,00GB','2.00GHz', applications)

print(n.info())
print(f"applications: {n.applications.info()}")