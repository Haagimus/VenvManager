import os

from guizero import App, Text, TextBox, PushButton, ListBox, Box

# Constants
app_bg = '#abbad9'
btn_bg = '#cbcbcb'


# Run the lsvirtualenv command and parse the output to the listbox
def list_virtualenvs():
	venv_list.clear()
	output = os.popen('lsvirtualenv')
	results = output.read().split('\n')[3:-2]
	for venv in results:
		venv_list.append(venv)


# Activate the selected venv
def activate_venv():
	pass


# Delete the selected venv
def delete_venv():
	confirm = app.yesno('Confirm action',
	                    f'Confirm deletion of venv:\n\n{venv_list.value}\n\nTHIS ACTION CANNOT BE UNDONE!!!')
	if confirm:
		os.popen(f'rmvirtualenv {venv_list.value}')
	else:
		venv_list.value = ''


# Create new venv using the name entered in the new_venv_name text input
def create_venv():
	if new_venv_name.value == '':
		pass
	else:
		os.popen(f'mkvirtualenv {new_venv_name.value}')
		print(new_venv_name.value)
		new_venv_name.clear()


app = App('VENV Manager', layout='grid', bg=app_bg)
app.height = 600
app.width = 520

"""Top padding"""
box = Box(app, grid=[0, 0], height=15, width='fill')
"""Left padding"""
box = Box(app, grid=[0, 0], height='fill', width=15)

"""Left content"""
# Get venv button
get_venvs = PushButton(app, list_virtualenvs, text='Load virtualenvs', grid=[1, 1], width=20)
get_venvs.text_size = 14
get_venvs.bg = btn_bg
box = Box(app, grid=[1, 2], height=15, width='fill')
# List box
venv_list = ListBox(app, align='left', grid=[1, 3], height=400, width=250)
venv_list.text_size = 14
venv_list.bg = 'white'
box = Box(app, grid=[1, 4], height=15, width='fill')
# Activate venv button
activate = PushButton(app, activate_venv, text='Activate', grid=[1, 5], align='left')
activate.text_size = 14
activate.bg = btn_bg
activate.width = 8
# Delete venv button
delete = PushButton(app, delete_venv, text='Delete', grid=[1, 5], align='right')
delete.text_size = 14
delete.bg = btn_bg
delete.width = 8

"""Center padding"""
box = Box(app, grid=[2, 1], height='fill', width=30)

"""Right content"""
new_label = Text(app, text='New VENV Name:', grid=[3, 1])
# New venv name texxt input
new_venv_name = TextBox(app, grid=[3, 2], width=20)
new_venv_name.text_size = 14
new_venv_name.bg = 'white'
# Create venv button
create_venv_button = PushButton(app, create_venv, text='Create venv', grid=[3, 3], align='left')
create_venv_button.text_size = 14
create_venv_button.bg = btn_bg

list_virtualenvs()

app.display()
