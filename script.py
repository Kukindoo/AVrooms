from selenium import webdriver
import time


#You need to be changing just here lines!
username = "email"
password =  "password"
rooms = [ "a226", "a227", "a308"]



url = "https://cityuni.service-now.com/sp?id=sc_cat_item&sys_id=e06c3bbddb34a0905fb52de74b961953"
login_username = """/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[1]/input"""
login_password = """/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[2]/input"""
login_button = """/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[4]/span"""

room =                  """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[1]/div/div/div/div/span/span[2]/div/div/a"""
room_select =           """/html/body/div[4]/ul/li/div"""
room_textfield =        """/html/body/div[4]/div/input"""
control_panel =         """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[2]/div/div/div[2]/div/span/div/a/span[2]"""
control_panel_select =  """/html/body/div[5]/ul/li[2]"""
echo =                  """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[2]/div/div/div[6]/div/span/div/a/span[2]"""
echo_select =           """/html/body/div[6]/ul/li[2]"""
laptop =                """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[2]/div/div/div[10]/div/span/div/a/span[2]"""
laptop_select =         """/html/body/div[7]/ul/li[2]"""
microphone =            """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[2]/div/div/div[14]/div/span/div/a/span[2]"""
microphone_select =     """/html/body/div[8]/ul/li[2]"""
monitor =               """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[2]/div/div/div[18]/div/span/div/a/span[2]"""
monitor_select =        """/html/body/div[9]/ul/li[2]"""
pod =                   """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[2]/div/div/div[22]/div/span/div/a/span[2]"""
pod_select =            """/html/body/div[10]/ul/li[2]"""
projector =             """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[2]/div/div/div[26]/div/span/div/a/span[2]"""
projector_select =      """/html/body/div[11]/ul/li[2]"""
type_of =               """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[3]/div/div/div[1]/div/span/div/a/span[2]"""
type_select =           """/html/body/div[12]/ul/li[3]"""
screen =                """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[4]/div/div/div[2]/div/span/div/a/span[2]"""
screen_select =         """/html/body/div[13]/ul/li[2]"""
visualiser =            """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[4]/div/div/div[6]/div/span/div/a/span[2]"""
visualiser_select =     """/html/body/div[14]/ul/li[2]"""
issue =                 """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[4]/div/div/div[11]/div/span/div/a/span[2]"""
issue_select =          """/html/body/div[15]/ul/li[2]"""
submit_button =         """/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span[1]/div/div/div[1]/div[2]/div/div[1]/div[3]/button"""


class Script:



    def __init__(self) -> None:
        self.browser = webdriver.Chrome()#chrome_options=options
        self.browser.implicitly_wait(30)
        print("starting browser...")
        self.browser.get(url)
        time.sleep(10)
        self.enterInInput(login_username, username)
        self.enterInInput(login_password, password)
        self.clickOnElement(login_button)


        for _room in rooms:
            self.select_all_working(_room)
            time.sleep(5)
            self.browser.get(url)
            time.sleep(1)
            print(f"Room {_room} logged sucessfully")
        print("all room finished")
        time.sleep(100)




        
        




    def enterInInput(self,xPath, text):
        element = self.browser.find_element_by_xpath(xPath)
        element.send_keys(text)
        
    def clickOnElement(self,xPath):
        element = self.browser.find_element_by_xpath(xPath)    
        element.click()

    def select_all_working(self, room_no):
        self.clickOnElement(room)
        self.enterInInput(room_textfield, room_no)
        time.sleep(1)
        self.clickOnElement(room_select)
        self.clickOnElement(control_panel)
        self.clickOnElement(control_panel_select)
        self.clickOnElement(echo)
        self.clickOnElement(echo_select)
        self.clickOnElement(laptop)
        self.clickOnElement(laptop_select)
        self.clickOnElement(microphone)
        self.clickOnElement(microphone_select)
        self.clickOnElement(monitor)
        self.clickOnElement(monitor_select)
        self.clickOnElement(pod)
        self.clickOnElement(pod_select)
        self.clickOnElement(projector)
        self.clickOnElement(projector_select)
        self.clickOnElement(type_of)
        self.clickOnElement(type_select)
        self.clickOnElement(screen)
        self.clickOnElement(screen_select)
        self.clickOnElement(visualiser)
        self.clickOnElement(visualiser_select)
        self.clickOnElement(issue)
        self.clickOnElement(issue_select)
        self.clickOnElement(submit_button)












if __name__ == "__main__":
    Script()