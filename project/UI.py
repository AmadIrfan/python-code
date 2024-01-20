from os import system
from random import choices


class UI:
    @staticmethod
    def MainMenu():
        print("Main Manu > ")
        print("(1) : Users Modules")
        print("(2) : Admin modules")
        print("(3) : Terms & Conditions")
        print("(4) : Exit")
        choise = input("Input : ")
        return str(choise)

    def tearmsCondition():
        print("Main Manu > Terms & Condition ")
        #     lines();
        print(" Rental Terms and Conditions ")
        print(
            "THESE TERMS AND CONDITIONS CONTAIN A BINDING ARBITRATION CLAUSE AND CLASS ACTION WAIVER THAT IMPACT YOUR RIGHTS ABOUT HOW TO RESOLVE DISPUTES. PLEASE READ THIS PROVISION CAREFULLY.\n"
        )
        print(
            "1. The Rental Agreement. These Rental Terms and Conditions, the rental document you receive when you are given access to the car you are renting (the  Rental Contract ) any additional agreement signed by you, any documents or agreements (or links to on-line documents or agreements) sent to you electronically in connection with your rental, the Privacy Notice, and the return receipt or record (the  Rental Receipt ) with computed rental charges together constitute the  Rental Agreement  between yourself and Avis Rent A Car System, LLC, or the independent Avis System Licensee identified on the Rental Contract (“Avis”).\n"
        )
        print(
            "2. Your Rental. You rent from Avis the car described on the Rental Contract, which rental is solely a transfer of possession, and not of drivership. You agree to the terms in the Rental Agreement provided any such term is not prohibited by the law of a jurisdiction covering this rental, in which case such law controls. “You” and “your” refer to the person who signs this agreement, “we”, “our” and “us” refer to Avis. You also agree that you are not our agent for any purpose; and that you cannot assign delegate  transfer your obligations under the Rental Agreement and any discrete part thereof.\n"
        )
        print(
            "3. Changes.Any change in the Rental Agreement or our rights must be in writing and signed by an authorized Avis officer.You further agree that we have the unilateral right to change these Terms and Conditions from time to time either upon written notice to you, in paper or electronic form, or upon our posting such changes on the Avis web site.Such changes will apply to rentals that you reserve after such notice has been given, as indicated by the date of such notice, if sent in written form, or the date such changes are posted on the Avis web site, which date will be indicated therein, without any requirement by you to sign the changed Terms and Conditions.Changes to these Terms and Conditions will be posted as they occur on the Avis web site at www.Avis.com and will govern all rentals commencing after posting even if the terms provided at time of reserving the rental car are different.\n"
        )
        print(
            "4. Meaning of Car.The word car in the Rental Agreement means the vehicle rented to you or its replacement and includes tires,tools,keys,key fobs, equipment, included and optional accessories, plates, documents, and any other products or property provided by Avis with the vehicle and separately rented to you by Avis unless otherwise explicitly specified in the Rental Agreement.\n "
        )

    def menuTop():
        print(
            "                                                                                        ___                ___                               "
        )
        print(
            "                           _______ _______ ___________    __________________  _______  /  /____________ __/  /                               "
        )
        print(
            "                          /   ___ /  ____   /  ______/   /  ________/    _  \\/  ___  \\/   __/ /  _____   /  /                              "
        )
        print(
            "                         /  /___ /  /___/  /  /         /  /       /     __ /  /  /  /  /____/  /____/  /  /____                             "
        )
        print(
            "                         \\______ \\_____^__/__/         /__/        \\_______/  /  /  /\\______/\\______^__/\\______/                       "
        )
        print(
            "                                                                                                                                             "
        )
        print(
            "                                                                            ___                                                              "
        )
        print(
            "                                                __________     ___________ /  /__________________   ____                                     "
        )
        print(
            "                                               / ______/ /    / / ________/  ___/   __   /   /___ '  ___\\                                   "
        )
        print(
            "                                              ( ____  / /____/ ( ______  /  /__/ /_____ /   /   /   /   /                                    "
        )
        print(
            "                                             /_______/\\_______/_________/_____/\\_______/___/   /___/   /                                   "
        )
        print(
            "                                                      ______ /                                                                               "
        )
        print(
            "                                                     /______/                                                                                "
        )
        print(
            "                                                                                                                                             "
        )

    def lines():
        print(">------------------------------------------- ")

    def clearScreen():
        input("Press Any Key to Continue.... ")
        system("cls")
        UI.menuTop()

    def WrongInput():
        print("You Enter Wrong input")
        choice = input("Input : ")
        return str(choice)
