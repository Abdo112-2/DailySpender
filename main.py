from flet import *

from database import Expenses ,sponsored

from datetime import datetime

from settings import Sg, Colors_settings, Currencies_settinegs, languages_settings

import random

import sqlite3 as sql

import csv


        

############# Connect database start #############

db = sponsored

conn = sql.connect('expenses.db', check_same_thread=False)
cur = conn.cursor()


############## Connect database end ##############

sg = Sg()

colors = Colors_settings()

language = languages_settings()

cur_sg = Currencies_settinegs()



### id var ###
id_expense: int = 0
##############

##### currency symbol fun #####
def currency_code():
    cur_sg = Currencies_settinegs()
    return cur_sg.currencies_mode()["symbol"]
    

##############################

##### language data fun ######
def language_datas():
    return language.langueage_data()

##############################


def main(page:Page):
    page.title = 'DailySpender'

    page.theme_mode = sg.read_settings()['Theme']

    page.rtl = language_datas()["rtl"]

    sg.system_mode_write(page.platform_brightness.value)
    
    
    ##### Home Variables start ####

    
    
    ### filter menu start ###
    
    ### filter menu end ###
        ##################
    ### amount textfield start ###
    amount_textfield: TextField= TextField(
        input_filter =  InputFilter(regex_string=r"^\d*\.?\d*$"),
        keyboard_type=KeyboardType.NUMBER,
        border_color=colors.colors_mode()["outline"], 
        border_radius=7,
        prefix_style=TextStyle(
            weight=FontWeight.BOLD, 
            size=17
        ), 
        text_style=TextStyle( 
            weight=FontWeight.W_600, 
            size=17
        ),
        
        

    )
    ### amount textfield end ###
        ##################
    ### category menu start ###
    category_menu:Dropdown = Dropdown(
        label=language_datas()["Add Expense"]["category options"]["label"],
        width=1420,
        
        border_color=colors.colors_mode()["outline"], 
        border_radius=7,
        text_style=TextStyle( weight=FontWeight.W_600, size=17),
        label_style=TextStyle( weight=FontWeight.W_600, size=17),
        select_icon=IconValue,
        options=[
            dropdown.Option(language_datas()["Add Expense"]["category options"]["title"], disabled=True,),
            dropdown.Option(language_datas()["Add Expense"]["category options"]["food text"], leading_icon=Icons.RESTAURANT),
            dropdown.Option(language_datas()["Add Expense"]["category options"]["transport text"], leading_icon=Icons.DIRECTIONS_BUS),
            dropdown.Option(language_datas()["Add Expense"]["category options"]["other text"], leading_icon=Icons.MORE_HORIZ)
        ]
    )
    ### category menu end ###
        #################
    ### note textfiled start ###
    note_textfield:TextField = TextField(
        multiline=True, 
        min_lines=2, 
        max_lines=2, 
        border_color=colors.colors_mode()["outline"], 
        border_radius=7 
    )
    ### note textfiled end ###



    ### add button start ###
    add_button: ElevatedButton = ElevatedButton(
        text=language_datas()["Add Expense"]["add button"],
        color = 'white',
        bgcolor= Colors.BLUE_700, 
        width=1420,
        height=40,
        style=ButtonStyle(shape=RoundedRectangleBorder(7)),
        disabled=True

    )

    ### add button end ###

    ##### update page variables ######

    ### amount textfield start ###
    amount_textfield_update: TextField= TextField(
        input_filter =  InputFilter(regex_string=r"^\d*\.?\d*$"),
        keyboard_type=KeyboardType.NUMBER,
        border_color=colors.colors_mode()["outline"], 
        border_radius=7,
        prefix_style=TextStyle(
            weight=FontWeight.BOLD, 
            size=17
        ), 
        text_style=TextStyle( 
            weight=FontWeight.W_600, 
            size=17
        ),
        
        

    )
    ### amount textfield end ###
        ##################
    ### category menu start ###
    category_menu_update:Dropdown = Dropdown(
        label=language_datas()["Update"]["category options"]["label"],
        width=1420,
        
        border_color=colors.colors_mode()["outline"], 
        border_radius=7,
        text_style=TextStyle( weight=FontWeight.W_600, size=17),
        label_style=TextStyle( weight=FontWeight.W_600, size=17),
        select_icon=IconValue,
        options=[
            dropdown.Option(language_datas()["Update"]["category options"]["title"], disabled=True,),
            dropdown.Option(language_datas()["Update"]["category options"]["food text"], leading_icon=Icons.RESTAURANT),
            dropdown.Option(language_datas()["Update"]["category options"]["transport text"], leading_icon=Icons.DIRECTIONS_BUS),
            dropdown.Option(language_datas()["Update"]["category options"]["other text"], leading_icon=Icons.MORE_HORIZ)
        ]
    )
    ### category menu end ###
        #################
    ### note textfiled start ###
    note_textfield_update:TextField = TextField(
        multiline=True, 
        min_lines=2, 
        max_lines=2, 
        border_color=colors.colors_mode()["outline"], 
        border_radius=7 
    )
    ### note textfiled end ###

    ### add button start ###
    
    update_button: ElevatedButton = ElevatedButton(
        text=language_datas()["Update"]["update button"],
        color = 'white',
        bgcolor= Colors.BLUE_700, 
        width=1420,
        height=40,
        style=ButtonStyle(shape=RoundedRectangleBorder(7)),
        disabled=True

    )

    ### add button end ###
    ##################################
    ### navigation darawer start ###
    global drawer_controls, drawer, sort_menu
    drawer_controls = [
        NavigationDrawerDestination(label=language_datas()["navigation drawer"]["home"], icon=Icons.HOME),
        NavigationDrawerDestination(label=language_datas()["navigation drawer"]["settings"], icon=Icons.SETTINGS),
        NavigationDrawerDestination(label=language_datas()["navigation drawer"]["about"], icon=Icons.INFO),
        Divider(),
        NavigationDrawerDestination(label=language_datas()["navigation drawer"]["exit"], icon=Icons.EXIT_TO_APP),
    ]
    drawer = NavigationDrawer(
        controls=drawer_controls,
        indicator_shape=RoundedRectangleBorder(0),
        tile_padding=Padding(0,0,0,0),
    )
    ### navigation darawer end ###

    ### theme switch start ###
    
    ### theme switch end ###
     ######################
    ### themms menu start ###
    themes_menu: Dropdown = Dropdown(
        width=1420,
        border_color=colors.colors_mode()["outline"], 
        border_radius=7,
        text_style=TextStyle( weight=FontWeight.W_600, size=17),
        value=language_datas()["Settings"]["theme options"][sg.read_settings()["Theme"]],
        options=[
            dropdown.Option(language_datas()["Settings"]["theme options"]['dark'], leading_icon=Icons.DARK_MODE,visible=True),
            dropdown.Option(language_datas()["Settings"]["theme options"]["light"], leading_icon=Icons.LIGHT_MODE),
            dropdown.Option(language_datas()["Settings"]["theme options"]["system"], leading_icon=Icons.SETTINGS_BRIGHTNESS)
        ]
    )
    ### themms menu end ###
    ### currency menu start ###
    currency_menu: Dropdown = Dropdown(
        width=1420,
        border_color=colors.colors_mode()["outline"], 
        border_radius=7,
        text_style=TextStyle(weight=FontWeight.W_600, size=17),
        value= sg.read_settings()["Currency"],
        options=[
            dropdown.Option("USD",f" {cur_sg.data()[1]["name"]}"),
            dropdown.Option("LYD",f" {cur_sg.data()[0]["name"]}"),
            dropdown.Option("SAR",f" {cur_sg.data()[2]["name"]}"),
            dropdown.Option("EUR",f" {cur_sg.data()[3]["name"]}"),
        ]
        
    )
    ### currency menu end ### 
       ###################
    ### language menu start ###
    language_menu: Dropdown = Dropdown(
        width=1420,
        border_color=colors.colors_mode()["outline"], 
        border_radius=7,
        text_style=TextStyle( weight=FontWeight.W_600, size=17),
        value=sg.read_settings()["Language"],
        options=[
            dropdown.Option("English"),
            dropdown.Option("العربية"),
        ]

    )
    ### language menu end ###


    #### show variables start ####
    amount_show: Text = Text(size=20)
    category_show: Text = Text(size=20)
    create_at_show = Text(size=20)
    update_at_show = Text(size=20)
    note_show: Text = Text(size=16, text_align=TextAlign.CENTER, width=1420)
    
    ##############################

    #### sort menu ####
    sort_menu = Dropdown(
        value=sg.sort_read(),
        border_width=0,
        width=200,
        options=[
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["title text"], disabled=True),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["all categories"]),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["food"]),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["transport"]),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["other"]),
 
        ]

        
    )
    ###################
    ###### Home Variables end #####
        ##################
        

    ###### nav drawer ######

    ############ Functions start ############

    def show_id(id):
        def show(e):
            global id_expense
            id_expense = id
            data_show = db.query(Expenses).filter(Expenses.id==id).first()

            amount_show.value = str(data_show.amount) + currency_code()
            category_show.value = language_datas()["Expenses"][data_show.category]
            date_time_create = datetime.strptime(str(data_show.create_at), '%Y-%m-%d %H:%M:%S')
            create_at_show.value = date_time_create.strftime('%d/%m/%Y')
            date_time_update = datetime.strptime(str(data_show.update_at), '%Y-%m-%d %H:%M:%S')
            update_at_show.value = date_time_update.strftime('%d/%m/%Y')
            note_show.value = data_show.note

            page.views.clear()
            page.go("/Show")

        page.update()
        return show

        
    def edit_id(id):
        global id_expense
        id_expense = id
        def edit(e):

            page.views.clear()
            data_by_id = db.query(Expenses).filter(Expenses.id==id).first()
            
            amount_textfield_update.value = data_by_id.amount
            category_menu_update.value = language_datas()["Expenses"][data_by_id.category]
            note_textfield_update.value = data_by_id.note

            page.go("/Update")
            page.update()

            
        page.update()
        return edit

    ##### delete id ######

    def delete_id(id):
        def delete(e):
            
            def delete_sure(e):
                db.commit()
                alert.open = False
                shows.controls.clear()
                [shows.controls.append(show) for show in reversed(show_data())]
                shows.update()
                page.go('/')
            def cancel_sure(e):
                db.close()
                alert.open = False
                shows.clean()
                [shows.controls.append(show) for show in reversed(show_data())]
                shows.update()
                page.go('/')
            db.query(Expenses).filter(Expenses.id == id).delete()
            alert = AlertDialog(
                
                content=Column(
                    
                    width=200,
                    spacing=20,
                    controls=[
                        Text(language_datas()["options ed"]["delete options"]["title text"], rtl=language_datas()['rtl'], size=22, width=240),
                        Container(

                            Row(
                
                                controls=[
                                    ElevatedButton(
                                        language_datas()["options ed"]["delete options"]["delete button"],
                                        expand=6,
                                        height=40,
                                        
                                        on_click=delete_sure,
                                        style=ButtonStyle(
                                            bgcolor=Colors.RED_700,
                                            shape=RoundedRectangleBorder(7),
                                            color=colors.colors_mode()["color"],
                                        ),
                                        
                                    ),
                                    OutlinedButton(
                                        language_datas()["options ed"]["delete options"]["cancel button"],
                                        expand=4,
                                        height=40,
                                        
                                        on_click=cancel_sure,
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(7),
                                            color=colors.colors_mode()["color"],
                                            
                                        ),
                                    )
                                ],
                            ),
                            rtl=language_datas()["rtl"],
                            width=300
                        ),
                        
                    ],
                    height=97
                    
                ),
                content_padding=Padding(20,13,20,0)
            )
            page.overlay.append(alert)
            alert.open = True
            page.update()

            
        
        db.close()
        page.update()
        return delete


    #####################
    def show_menu(index: int):
        
        def handler(e):
            menu = AlertDialog(
                
                actions=[
                    Column(
                        spacing=10,
                        controls=[
                            Text(language_datas()["options ed"]["title menu"], rtl=language_datas()['rtl'], size=27, width=300),
                            Column(
                        horizontal_alignment=CrossAxisAlignment.START,
                        controls=[
                            TextButton(
                                content=Row(controls=[Icon(Icons.EDIT, size=20), Text(language_datas()["options ed"]["options"]["Edit text"], size=20)], rtl=language_datas()["rtl"]),
                                height=45,
                                width=300,
                                
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(0),
                                    padding=Padding(28,True,28,True)
                                    
                                ),
                                on_click = edit_id(index)
                               
                            ),

                            TextButton(
                                content=Row(controls=[Icon(Icons.DELETE, size=20), Text(language_datas()["options ed"]["options"]["Delete text"], size=20)], rtl=language_datas()["rtl"]),
                                height=45,
                                width=300,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(0),                                    
                                    padding=Padding(28,True,28,True)
                                ),
                                on_click = delete_id(index)                   
                                
                                
                                
                            ),
                            TextButton(
                                content=Row(controls=[Icon(Icons.VISIBILITY, size=20), Text(language_datas()["options ed"]["options"]["Show text"], size=20)], rtl=language_datas()["rtl"]),
                                height=45,
                                width=300,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(0),                                    
                                    padding=Padding(28,True,28,True)
                                ),
                                on_click = show_id(index)                   
                                
                                
                                
                            )
                        ],
                        rtl=language_datas()["rtl"],
                        spacing=0

                        
                        
                    ),
                        ],
                        
                    ),
                    
                ],
                actions_alignment=MainAxisAlignment.START,
                actions_padding=Padding(0,10,0,22),
                
                
            )
            menu.open = True
            page.overlay.append(menu)
            page.update()
            
        return handler
            
    def show_data():

        sort_auto = str(language_datas()["Expenses"]["menu app bar"]["options"]["sort filters"][sg.sort_read()])
        
        data = conn.execute(f"SELECT * FROM expenses WHERE category = '{sort_auto}' OR '{sort_auto}' = 'all' ")
        columns  = []
        columns.clear()
        for i in (data):
            id = i[0]
            amount = i[1]
            category = i[2]
            note = i[3]
            date_time = datetime.strptime(str(i[5]), '%Y-%m-%d %H:%M:%S')
            date = date_time.strftime('%d/%m/%Y')
        
            show = Container(

                
                Column(
                    
                        controls=[
                            
                            Row(
                                controls=[

                                    Text(
                                        language_datas()["Expenses"][category],
                                        weight=FontWeight.BOLD,
                                        size=16,
                                        
                                        
                                    ),
                                    Text(
                                        str(amount) + ' ' + currency_code(),
                                        weight=FontWeight.BOLD,
                                        size=16,
                                        
                                        
                                    ),
                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN
                            ),
                        
                            Row(
                                controls=[
                                    Text(
                                        note,
                                        size=14,
                                        expand=3,
                                        text_align=TextAlign.START,
                                        overflow=TextOverflow.ELLIPSIS
                                    ),
                                    Text(
                                        date,
                                        size=14,
                                        expand=7,
                                        text_align=TextAlign.END,
                                    ),
                                                                     
                                ],
                                
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                
                            ),
                            Divider(),
                            
                            
                        ],
                        spacing=10,
                    
                ),
                on_long_press=show_menu(id),
                
                
            )
            columns.append(show)
            
            
        return columns
            
            

    ########### add expenses func ###########
    def add_expense(e):
        
        new_expense = Expenses(
            amount = amount_textfield.value,
            category = category_menu.value,
            note = note_textfield.value,
        )
        db.add(new_expense)
        db.commit() 
        db.close()

        amount_textfield.value = None
        category_menu.value = None
        note_textfield.value = None
        add_button.disabled=True
        
        
        
        page.go('/')
    
    ############ update expenses func ##################
    def update_expenses(e):
        
        
        amount = amount_textfield_update.value
        note = note_textfield_update.value
        category = category_menu_update.value

        data_update = {
            Expenses.amount: amount,
            Expenses.category: category,
            Expenses.note: note
        }

        db.query(Expenses).filter(Expenses.id == id_expense).update(data_update)

        db.commit()

        
        page.go("/")
    ###### text field onchange ###### 
    
    def validate(e):
        if all([amount_textfield.value, category_menu.value]):
            add_button.disabled = False
        else:
            add_button.disabled = True

        page.update()
    
    def validate_update(e):
        if all([amount_textfield_update.value, category_menu_update.value]):
            update_button.disabled = False
        else:
            update_button.disabled = True

        page.update()
    
    def nav_drawer_oc(e):
        select_index = drawer.selected_index
        if select_index == 0:
            page.go(route='/')
        elif select_index == 1:
            page.go(route='/Settings')
        elif select_index == 2:
            page.go(route='/About')
        else:
            page.window.close()
    

    ##### clear all expenses start #####
    def clear_all(e):
        db.close()
        
        def delete_sure(e):
                db.commit()
                alert.open = False
                page.go("/")
                drawer.selected_index = 0
                page.update()
        def cancel_sure(e):
            db.close()
            alert.open = False
            page.go("/Settings")
            drawer.selected_index = 1
            page.update()
        db.query(Expenses).delete()
        alert = AlertDialog(
                
                content=Column(
                    
                    width=200,
                    spacing=20,
                    controls=[
                        Text(language_datas()["options ed"]["delete options"]["title text"], rtl=language_datas()['rtl'], size=22, width=240),
                        Container(
                            
                            Row(
                
                                controls=[
                                    ElevatedButton(
                                        language_datas()["options ed"]["delete options"]["delete button"],
                                        expand=6,
                                        height=40,
                                        
                                        on_click=delete_sure,
                                        style=ButtonStyle(
                                            bgcolor=Colors.RED_700,
                                            shape=RoundedRectangleBorder(7),
                                            color=colors.colors_mode()["color"],
                                        ),
                                        
                                    ),
                                    OutlinedButton(
                                        language_datas()["options ed"]["delete options"]["cancel button"],
                                        expand=4,
                                        height=40,
                                        
                                        on_click=cancel_sure,
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(7),
                                            color=colors.colors_mode()["color"],
                                            
                                        ),
                                    )
                                ],
                            ),
                            rtl=language_datas()["rtl"],
                            width=300,
                            
                        ),
                        
                    ],
                    height=97,
                
                    
                ),
                content_padding=Padding(20,13,20,0)
        )
        alert.open = True
        page.overlay.append(alert)
        page.update()
        
    ##### clear all expenses end #####
    
    ##### save button start #####
    def save_click(e):
        global drawer_controls, drawer, sort_menu

        theme = themes_menu.value
        theme = language_datas()["Settings"]["theme options a"][theme]
        currency = currency_menu.value
        language = language_menu.value

        sg.update_settings(Theme=theme, Currency=currency, Language=language)

        page.theme_mode = sg.read_settings()['Theme']
        colors = Colors_settings()
        page.rtl = language_datas()["rtl"]

        themes_menu.value=language_datas()["Settings"]["theme options"][sg.read_settings()["Theme"]]
        themes_menu.update()
    # إعادة بناء drawer_controls بالقيم الجديدة للغة
        drawer_controls = [
            NavigationDrawerDestination(label=language_datas()["navigation drawer"]["home"], icon=Icons.HOME),
            NavigationDrawerDestination(label=language_datas()["navigation drawer"]["settings"], icon=Icons.SETTINGS),
            NavigationDrawerDestination(label=language_datas()["navigation drawer"]["about"], icon=Icons.INFO),
            Divider(),
            NavigationDrawerDestination(label=language_datas()["navigation drawer"]["exit"], icon=Icons.EXIT_TO_APP),
        ]
        drawer.controls.clear()
        [drawer.controls.append(control) for control in drawer_controls]
        page.drawer = drawer

        # إعادة بناء themes_menu بالقيم الجديدة للغة
        themes_menu.options = [
            dropdown.Option(language_datas()["Settings"]["theme options"]['dark'], leading_icon=Icons.DARK_MODE, visible=True),
            dropdown.Option(language_datas()["Settings"]["theme options"]["light"], leading_icon=Icons.LIGHT_MODE),
            dropdown.Option(language_datas()["Settings"]["theme options"]["system"], leading_icon=Icons.SETTINGS_BRIGHTNESS)
        ]

        # إعادة بناء sort_menu بالقيم الجديدة للغة
        sort_menu.options = [
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["title text"], disabled=True),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["all categories"]),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["food"]),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["transport"]),
            dropdown.Option(language_datas()["Expenses"]["menu app bar"]["options"]["sort menu"]["other"]),
        ]
        sort_menu.value = sg.sort_read()
        
        cur_sg = Currencies_settinegs()
        currency_menu.options.clear()
        options_cur=[
            dropdown.Option("USD",f" {cur_sg.data()[1]["name"]}"),
            dropdown.Option("LYD",f" {cur_sg.data()[0]["name"]}"),
            dropdown.Option("SAR",f" {cur_sg.data()[2]["name"]}"),
            dropdown.Option("EUR",f" {cur_sg.data()[3]["name"]}"),
        ]
        [currency_menu.options.append(option_cur) for option_cur in options_cur]
        currency_menu.update()

        page.go("/")
        drawer.selected_index = 0
        page.update()

    ##### save button end #####
    
    ##### cancel button start #####

    def cancel_click(e):
        values = sg.read_settings()
        themes_menu.value = values['Theme']
        currency_menu.value = values['Currency']
        language_menu.value = values['Language']

        page.go('/')
        drawer.selected_index = 0
        
        
        
    ##### cancel button end #####

    
    def sort_data(e):
        pass

    ###################
    #### create csv file ####
    def csv_Export(e):
        save_dialog = FilePicker()
        
        page.overlay.append(save_dialog) 
        page.update()
        
        def export_file(e:FilePickerResultEvent):
            
            
            if e.path:
                datas = list(cur.execute('SELECT * FROM expenses'))
                with open(e.path, 'w', newline="", encoding="utf-8") as file:
                    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    title_rows = language_datas()["csv file"]["title rows"]
                    writer.writerow((title_rows["amount"], title_rows["category"], title_rows["note"], title_rows["created at"], title_rows["updated at"]))

                    for data in datas:
                        row_data = [None, None, None, None, None]

                        amount = data[1]
                        category = data[2]
                        note = data[3]

                        create_at_format = datetime.strptime((data[4]), "%Y-%m-%d %H:%M:%S")
                        create_at = create_at_format.strftime('%d/%m/%Y')

                        update_at_format = datetime.strptime((data[5]), "%Y-%m-%d %H:%M:%S")
                        update_at = update_at_format.strftime('%d/%m/%Y')
                        
                        row_data[0] = amount
                        row_data[1] = category
                        row_data[2] = note
                        row_data[3] = create_at
                        row_data[4] =update_at

                        writer.writerow(row_data)
                        row_data = [None, None, None, None, None]
        
        save_dialog.on_result = export_file

        random_number_1 = random.randrange(10000,99999)
        random_number_2 = random.randrange(10000,99999)
        name_file = "DYSR_" + str(random_number_1) + '_' + str(random_number_2)
        
        save_dialog.save_file(file_name=name_file+'.csv', allowed_extensions=["csv"])
        page.update()
    #########################
    shows = Column(
                scroll=True,
            )
    
    [shows.controls.append(show) for show in reversed(show_data())]
    

    ####### sorting function ######
    def sorting_func(e):
        
        SORT = sort_menu.value
        sg.sort_write(SORT)

        shows.controls.clear()
        [shows.controls.append(show) for show in reversed(show_data())]
        page.update()

        
    ###############################

    ############# Functions end #############

    def route_change(e):
        page.views.clear()
        ############# Home Page #############
        shows.controls.clear()
        [shows.controls.append(show) for show in reversed(show_data())]
        

        page.views.append(
            View(
                route='/',
                drawer=drawer,
                
                appbar=AppBar(

                    
                    bgcolor=Colors.BLUE_700,
                    color= Colors.WHITE70,
                    actions=[
                        IconButton(icon=Icons.ADD, on_click= lambda _: page.go('/Add_page')),
                        
                        PopupMenuButton(
                            items=[
                                PopupMenuItem(language_datas()["Expenses"]["menu app bar"]["options"]["csv file text"], on_click = csv_Export),
                                PopupMenuItem(content=sort_menu),
                            ],
                            tooltip=language_datas()["Expenses"]["menu app bar"]["tooltip text"],
                            

                        ),
                        Container(width=7),
                    ],
                    
                ),
                controls=[
                    Container(
                        Column(
                            controls=[
                                
                                Text(value=language_datas()["Expenses"]["title text"], size=22, weight=FontWeight.BOLD),
                                Container(
                                    shows,
                                    
                                    padding=Padding(16,16,16,16),
                                    border = Border(BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"])),
                                    border_radius=7,
                                    width=1420,
                                    height=490,
                                    margin=Margin(0,10,0,0),
                                    
                                ),
                            ]
                        ),
                        margin=Margin(4, 30, 4, 0),
                    ),
                ]
            )
        )
        ###################### Add Expenses Page ######################
        if page.route == '/Add_page':
            page.views.append(
                View(
                    route='/Add_page',
                    ## Appbar Start ##
                    appbar=AppBar(
                        center_title=True,
                        title=Text(
                            value=language_datas()["Add Expense"]["title appbar"],
                            size=21, italic=True,
                            weight=FontWeight.W_400,
                            ),
                        bgcolor=Colors.BLUE_700,
                        color= Colors.WHITE70,
                        ),
                    ## Appbar End ##
                    controls=[
                        Container(
                            
                            Column(
                                controls=[
                                    Text(language_datas()["Add Expense"]["title text"], size=22, weight=FontWeight.BOLD),
                                    Container(
                                        Column(
                                            controls=[
                                                Text(language_datas()["Add Expense"]["amount text"], weight=FontWeight.W_600,),
                                                amount_textfield, ##### Amount Entry
                                                Text(language_datas()["Add Expense"]["category text"], weight=FontWeight.W_600,),
                                                category_menu, ##### Category Menu
                                                Text(language_datas()["Add Expense"]["note text"], weight=FontWeight.W_600,),
                                                note_textfield, ##### Note Entry
                                                add_button,
                                            ],
                                        ),
                                        padding=Padding(16,25,16,16),
                                        border = Border(BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"])),
                                        border_radius=7,
                                    )  
                                ],
                            ),
                            margin= Margin(left = 12, right=12, top = 30 , bottom=False)
                        )
                    ]
                )
            )
        elif page.route == '/Settings':
            
            page.views.append(
                View(
                    route='/Settings',
                    appbar=AppBar(
                        bgcolor=Colors.BLUE_700,
                        color=Colors.WHITE70,
                        title=Text(
                            value=language_datas()["Settings"]["title appbar"],
                            size=21, italic=True,
                            weight=FontWeight.W_400
                            ),
                        center_title=True
                    ),
                    drawer=drawer,
                    controls=[
                        Container(
                            Column(
                                controls=[
                                    Text(language_datas()["Settings"]["title text"], size=25, weight=FontWeight.BOLD),
                                    Container(
                                        Column(
                                            spacing=15,
                                            controls=[
                                                Text(language_datas()["Settings"]["theme text"], size=17, weight=FontWeight.BOLD),
                                                themes_menu,
                                                Text(language_datas()["Settings"]["currency text"], size=17, weight=FontWeight.BOLD),
                                                currency_menu,
                                                Text(language_datas()["Settings"]["language text"], size=17, weight=FontWeight.BOLD),
                                                language_menu,
                                               
                                                OutlinedButton(
                                                    text=language_datas()["Settings"]["clear all expenses button"],
                                                    width=1420,
                                                    height=40,
                                                    style=ButtonStyle(
                                                        colors.colors_mode()["color"],
                                                        shape=RoundedRectangleBorder(7),
                                                        side=BorderSide(1, color=Colors.RED_900),
                                                        overlay_color=Colors.RED_900,
                                                        
                                                        text_style=TextStyle(
                                                            size=17,
                                                            
                                                        )
                                                        
                                                    ),
                                                    on_click= clear_all,
                                                    
                                                ),
                                                Container(
                                                    Row(
                                                        controls=[
                                                            ElevatedButton(
                                                                language_datas()["Settings"]["save changes button"],
                                                                color='white',
                                                                height=40,
                                                                bgcolor=Colors.BLUE_700,
                                                                expand=6,
                                                                style=ButtonStyle(
                                                                    overlay_color=Colors.BLUE_600,
                                                                    shape = RoundedRectangleBorder(7),
                                                                    text_style=TextStyle(
                                                                        size=17,
                                                                    )
                                                                ),
                                                                on_click=save_click ,
                                                            ),
                                                            OutlinedButton(
                                                                language_datas()["Settings"]["cancel button"],
                                                                height=40,
                                                                expand=4,
                                                                style=ButtonStyle(
                                                                    color=colors.colors_mode()["color"],
                                                                    shape=RoundedRectangleBorder(7),
                                                                    side=BorderSide(1, color= colors.colors_mode()["outline"]),
                                                                    overlay_color=colors.colors_mode()["outline"], 
                                                                    text_style=TextStyle(
                                                                        size=20,
                                                                    )
                                                                ),
                                                                on_click=cancel_click,
                                                            
                                                            )
                                                        ],
                                                    ),
                                                    padding=Padding(0,10,0,0),
                                                    width=1420,
                                                )
                                            ]
                                        ),
                                        padding=Padding(0,12,0,0)
                                    )
                                ]
                            ),margin=Margin(12,22,12,False)
                        )
                    ]
                )
            )

        elif page.route == '/Update':
            page.views.append(
                View(
                    route='/Update',
                    ## Appbar Start ##
                    appbar=AppBar(
                        center_title=True,
                        title=Text(
                            value=language_datas()["Update"]["title appbar"],
                            size=21, italic=True,
                            weight=FontWeight.W_400,
                            ),
                        bgcolor=Colors.BLUE_700,
                        color= Colors.WHITE70,
                    ),
                    ## Appbar End ##
                    controls=[
                        Container(
                            
                            Column(
                                controls=[
                                    Text(language_datas()["Update"]["title text"], size=22, weight=FontWeight.BOLD),
                                    Container(
                                        Column(
                                            controls=[
                                                Text(language_datas()["Update"]["amount text"], weight=FontWeight.W_600,),
                                                amount_textfield_update, ##### Amount Entry
                                                Text(language_datas()["Update"]["category text"], weight=FontWeight.W_600,),
                                                category_menu_update, ##### Category Menu
                                                Text(language_datas()["Update"]["note text"], weight=FontWeight.W_600,),
                                                note_textfield_update, ##### Note Entry
                                                update_button,
                                            ],
                                        ),
                                        padding=Padding(16,25,16,16),
                                        border = Border(BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"])),
                                        border_radius=7,
                                        
                                    )  
                                ],
                            ),
                            margin= Margin(left = 12, right=12, top = 30 , bottom=False)
                        )
                    ]
                    
                    
                )
            )
        elif page.route == "/Show":
            page.views.append(
                View(
                    route="/Show",
                    ## Appbar Start ##
                    appbar=AppBar(
                        center_title=True,
                        title=Text(
                            value=language_datas()["Update"]["title appbar"],
                            size=21, italic=True,
                            weight=FontWeight.W_400,
                            ),
                        bgcolor=Colors.BLUE_700,
                        color= Colors.WHITE70,
                    ),
                    ## Appbar End ##
                    controls=[
                        Container(
                            Column(
                                controls=[
                                    Row(
                                        controls=(
                                            Text(
                                                language_datas()["Show"]["amount text"], 
                                                weight=FontWeight.BOLD, 
                                                size=20
                                            ),
                                            amount_show
                                        ),
                                        width=1420,
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                        
                                    ),
                                    Row(
                                        controls=(
                                            Text(
                                                language_datas()["Show"]["category text"], 
                                                weight=FontWeight.BOLD, 
                                                size=20
                                            ),
                                            category_show
                                        ),
                                        width=1420,
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Row(
                                        controls=(
                                            Text(
                                                language_datas()["Show"]["create at text"], 
                                                weight=FontWeight.BOLD, 
                                                size=20
                                            ),
                                            create_at_show
                                        ),
                                        width=1420,
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Row(
                                        controls=(
                                            Text(
                                                language_datas()["Show"]["update at text"], 
                                                weight=FontWeight.BOLD, 
                                                size=20
                                            ),
                                            update_at_show
                                        ),
                                        width=1420,
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Column(
                                        controls=(
                                            Text(
                                                language_datas()["Show"]["note text"], 
                                                weight=FontWeight.BOLD, 
                                                size=20
                                            ),
                                            Container(
                                                Column(
                                                    controls=[note_show],
                                                    scroll=True
                                                ),
                                                border = Border(BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"]),BorderSide(2,colors.colors_mode()["outline"])),
                                                border_radius=7,
                                                padding=Padding(16,16,16,16),
                                                height=320,
                                                margin=Margin(0,15,0,0),
                                                width=1420
                                                
                                                
                                            )
                                        ),

                                    )
                                    
                                    

                                ]
                            ),
                            margin=Margin(15,15,15,15),
                            padding=Padding(10,10,10,10)
                        )
                    ]
                )
            )
        
        
        elif page.route == '/About':
            page.views.append(
                View(
                    route='/About',
                    appbar=AppBar(
                        bgcolor=Colors.BLUE_700,
                        color=Colors.WHITE70,
                        title=Text(
                            value="About",
                            size=21, italic=True,
                            weight=FontWeight.W_400
                            ),
                        center_title=True,
                    ),
                    drawer=drawer,
                    controls=[
                        Container(
                            Column(
                                controls=[
                                    Container(
                                        Text("About", size=25, weight=FontWeight.BOLD),
                                        margin=Margin(0,20,0,20)
                                    ),
                                    Row(
                                        controls=[
                                            Text("App name"),
                                            Text("DailySpender")
                                        ],
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Row(
                                        controls=[
                                            Text("Version"),
                                            Text("1.0.0")
                                        ],
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Row(
                                        controls=[
                                            Text("Developer"),
                                            Text("Abdullah Ahmed")
                                        ],
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Row(
                                        controls=[
                                            Text("Team"),
                                            Text("INFORTIK Dev Team")
                                        ],
                                        alignment=MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                    Container(
                                        Text("Why this app", weight=FontWeight.BOLD, size=20),
                                        margin=Margin(0,6,0,6)
                                    ),
                                    
                                    Text("""DailySpender helps you track your daily expenses with ease and claririty.it's designed for simplicity, accuracy and a better financial overview.""", size=15),
                                    Row(
                                        controls=[
                                            IconButton(icon=Icons.LANGUAGE, icon_color=colors.colors_mode()["color"]),
                                            Text("wwww.dailyspender.com"),
                                        ]
                                    ),
                                    
                                    Row(
                                        controls=[
                                            IconButton(icon=Icons.FACEBOOK, icon_color=colors.colors_mode()["color"], url="https://www.facebook.com/share/1N5ZiKSnew/"),
                                            Text("facebook")
                                        ]
                                    ),

                                    Row(
                                        controls=[
                                            IconButton(icon=Icons.CHALET_ROUNDED, icon_color=colors.colors_mode()["color"], url="https://api.whatsapp.com/send?phone=%2B218946028912"),
                                            Text("WhatsApp")
                                        ]
                                    ),
                                ]
                            ),
                            margin=Margin(10,10,0,10),
                        )
                    ]
                )
            )

        page.update()


    sort_menu.on_change = sorting_func
    

    
    amount_textfield.on_change = validate
    category_menu.on_change = validate
    add_button.on_click = add_expense

    amount_textfield_update.on_change = validate_update
    category_menu_update.on_change = validate_update
    note_textfield_update.on_change = validate_update
    update_button.on_click = update_expenses


    drawer.on_change=nav_drawer_oc

    
    
    ## Appbar Start ##
                
                
    ## Appbar End ##
    

    def page_go(e):
        page.views.pop()
        back_page = page.views[-1]
        page.go(back_page.route)
    
    
    


    page.on_route_change = route_change
    page.on_view_pop = page_go
    page.go(page.route)
if __name__ == '__main__':
    app(target=main, name="DailySpender")