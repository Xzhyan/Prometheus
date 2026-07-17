import subprocess

# core
from core.logger import addlog
from core.constants import Colors, SHORTS_JSON
from core.exceptions import ShortNotFoundError

# ui
from ui.ui_console import alert, list_commands

# utils/system
from utils.system import shutdown, restart, clear

# functions
from utils.functions import read_json, write_json


class CustomShort:
    def __init__(self, args):
        self.running = True

        self.commands = {
            'add': {
                'desc': "adiciona um novo atalho",
                'handler': self.add_short
            },
            'list': {
                'desc': "lista os atalhos adicionados",
                'handler': self.list_shorts
            },
            'remove': {
                'desc': "remove um atalho",
                'handler': self.remove
            }
        }

        self.manage()

    def add_short(self):
        type_ = input(f"  {Colors.TEXT}↪ {Colors.TITLE}tipo: app/dir {Colors.TEXT} > ")
        name = input(f"  {Colors.TEXT}↪ {Colors.TITLE}nome do atalho {Colors.TEXT} > ")
        path = input(f"  {Colors.TEXT}↪ {Colors.TITLE}caminho do atalho {Colors.TEXT} > ")

        if not type_ or not name or not path:
            response = "todos os campos devem ser preenchidos"
            addlog('info', f"SHORT_MODULE | {response}")
            alert('info', response)
            return

        data = read_json(SHORTS_JSON)

        for category, shorts in data.items():
            for short in shorts:
                if short['name'] == name:
                    alert('info', "já existe um atalho com esse nome")
                    return

        # verificar opções para evitar problema no type_
        data[type_].append({
            'name': name,
            'path': path
        })

        write_json(SHORTS_JSON, data)

        response = "novo atalho adicionado"
        addlog('success', f"SHORT_CREATE | {response}")
        alert('success', response)

        self.running = False

    def list_shorts(self):
        data = read_json(SHORTS_JSON)

        for category, shorts in data.items():
            print(f"\n{Colors.TEXT}[+] {Colors.ONE}{category}")

            for short in shorts:
                print(f" {Colors.TEXT}↪ {Colors.TITLE}{short['name']}")

        self.running = False

    def remove(self):
        name = input(f"  {Colors.TEXT}↪ {Colors.TITLE}nome do atalho {Colors.TEXT} > ")

        if not name:
            response = "todos os campos devem ser preenchidos"
            addlog('info', f"SHORT_MODULE | {response}")
            alert('info', response)
            return

        data = read_json(SHORTS_JSON)

        found = False

        for category, shorts in data.items():
            for short in shorts:
                if short['name'] == name:
                    shorts.remove(short)
                    found = True
                    break

            if found:
                break

        if not found:
            response = f"esse atalho não existe"
            addlog('error', response)
            alert('error', response)
            return
        
        write_json(SHORTS_JSON, data)
        
        response = f"o atalho {name} foi removido"
        addlog('success', response)
        alert('success', response)
        
        self.running = False

    def manage(self):
        while self.running:
            list_commands('Comandos do modulo de atalhos', self.commands)

            try:
                cmd = input(F" \n {Colors.TITLE}custom short {Colors.TEXT}> ")

                if cmd in self.commands:
                    self.commands[cmd]['handler']()
                
                else:
                    self.running = False

            except Exception as e:
                response = str(e)
                
                addlog('error', f"UNKNOWN_ERROR | {response}")
                alert('error', response)
            
            except KeyboardInterrupt:
                self.running = False

                response = "modulo de atalhos finalizado..."

                addlog('info', f"SHORT_MODULE | {response}")
                alert('info', response)


def open_short(args):
    """abre o atalho especificado"""

    type_ = args[0] # tipo code/explorer/app
    short_name = args[1]
    path = None

    data = read_json(SHORTS_JSON)


    for category, item in data.items():
        for short in item:
            if short['name'] == short_name:
                path = short['path']
                break

    if path == None:
        raise ShortNotFoundError("atalho inexistente")
    
    cmds = {
        'code': 'code',
        'explorer': 'start',
        'open': 'start'
    }

    cmd = cmds.get(type_, 'start')

    try:
        subprocess.Popen(f'{cmd} "" "{path}"', shell=True)
    
    except Exception as e:
        addlog('error', str(e))
        alert('error', str(e))


DEFAULT_COMMANDS = {
    'exit': {
        'desc': "finalizar a ferramenta",
        'handler': shutdown
    },
    'restart': {
        'desc': "finaliza o processo atual e inicia um novo",
        'handler': restart
    },
    'clear': {
        'desc': "limpar a tela",
        'handler': clear
    },
    'short': {
        'desc': "inicia o modulo de atalhos",
        'handler': CustomShort
    },
    'code': {
        'desc': "abre o code na pasta do atalho",
        'handler': lambda args: open_short(args)
    },
    'explorer': {
        'desc': "abre o explorer na pasta do atalho",
        'handler': lambda args: open_short(args)
    },
    'open': {
        'desc': "abre o aplicativo se o atalho for um",
        'handler': lambda args: open_short(args)
    }
}
