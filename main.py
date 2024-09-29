import classes
import commands

def work():
    productStorage1 = classes.ProductStorage("Пельмени от Андрея" ,[])
    prorab = classes.Prorab({
        "add": commands.AddCommand(productStorage1),
        "list": commands.ListCommand(productStorage1),
        "remove": commands.RemoveCommand(productStorage1),
        "help": commands.HelpCommand(productStorage1)
    })

    while True:
        command_input = input()
        command_itog = classes.CommandInput(command_input)

        if command_itog.command in prorab.spisok:
            prorab.spisok[command_itog.command].execute(command_itog.params)
        else:
            print("Такой команды нет!")

if __name__ == "__main__":
    work()