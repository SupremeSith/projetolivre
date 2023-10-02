from classe import *
import os

def main():
    while True:
        try:
            print("Bem vindo ao Valorant. Deseja ver o manual de:\n1- Mapas\n2- Personagens\n3- Sair")
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida")
            continue
        
        if opcao == 1:
            try:
                os.system("cls")
                print("Selecione um dos seguintes mapas:\n1- Ascent\n2- Bind\n3- Haven\n4- Split\n5- Icebox\n6- Breeze\n7- Fracture\n8- Pearl\n9- Lotus")
                d = int(input("Sobre qual mapa deseja aprender? "))
                os.system("cls")
                try:
                    match d:
                        case 1:
                            Ascent.Mapas()
                            Ascent.descrever_mapa()
                            os.system("pause")
                            os.system("cls")
                            

                        case 2:
                            Bind.Mapas()
                            Bind.descrever_mapa()
                            os.system("pause")
                            os.system("cls")

                        case 3:
                            Haven.Mapas()
                            Haven.descrever_mapa()
                            os.system("pause")
                            os.system("cls")

                        case 4:
                            Split.Mapas()
                            Split.descrever_mapa()
                            os.system("pause")
                            os.system("cls")

                        case 5:
                            Icebox.Mapas()
                            Icebox.descrever_mapa()
                            os.system("pause")
                            os.system("cls")

                        case 6:
                            Breeze.Mapas()
                            Breeze.descrever_mapa()
                            os.system("pause")
                            os.system("cls")

                        case 7:
                            Fracture.Mapas()
                            Fracture.descrever_mapa()
                            os.system("pause")
                            os.system("cls")

                        case 8:
                            Pearl.Mapas()
                            Pearl.descrever_mapa()
                            os.system("pause")
                            os.system("cls")

                        case 9:
                            Lotus.Mapas()
                            Lotus.descrever_mapa()
                            os.system("pause")
                            os.system("cls")
                except ValueError:
                    print("Opção inválida")
                    

            except ValueError:
                print("Opção inválida")
               
        
        elif opcao == 2:
            try:
                print("Selecione um dos seguintes agentes:\n1- Jett\n2- Raze\n3- Sage\n4- Cypher\n5- Sova\n6- Brimstone\n7- Omen\n8- Phoenix\n9- Viper\n10- Breach\n11- Reyna\n12- Killjoy\n13- Skye\n14- Yoru\n15- Astra\n16- Kay/o\n17- Neon\n18- Chamber\n19- Deadlock\n20- Gekko")
                c = int(input("Sobre qual personagem deseja aprender? "))
                os.system("cls")
                try:
                    match c:
                        case 1:
                            Jett.mostrar_habilidade()
                            Jett.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")


                        case 2:
                            Raze.mostrar_habilidade()
                            Raze.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")


                        case 3:
                            Sage.mostrar_habilidade()
                            Sage.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 4:
                            Cypher.mostrar_habilidade()
                            Cypher.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 5:
                            Sova.mostrar_habilidade()
                            Sova.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 6:
                            Brimtone.mostrar_habilidade()
                            Brimtone.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 7:
                            Omen.mostrar_habilidade()
                            Omen.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 8:
                            Phoenix.mostrar_habilidade()
                            Phoenix.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 9:
                            Viper.mostrar_habilidade()
                            Viper.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 10:
                            Breach.mostrar_habilidade()
                            Breach.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 11:
                            Reyna.mostrar_habilidade()
                            Reyna.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 12:
                            Killjoy.mostrar_habilidade()
                            Killjoy.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 13:
                            Skye.mostrar_habilidade()
                            Skye.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 14:
                            Yoru.mostrar_habilidade()
                            Yoru.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 15:
                            Astra.mostrar_habilidade()
                            Astra.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 16:
                            Kayo.mostrar_habilidade()
                            Kayo.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 17:
                            Neon.mostrar_habilidade()
                            Neon.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 18:
                            Chamber.mostrar_habilidade()
                            Chamber.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 19:
                            Deadlock.mostrar_habilidade()
                            Deadlock.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")

                        case 20:
                            Gekko.mostrar_habilidade()
                            Gekko.Listar_Habilidades_1()
                            os.system("pause")
                            os.system("cls")
                except ValueError:
                    print("Opção inválida")

            except ValueError:
                print("Opção inválida")
        
        elif opcao == 3:
            print("Obrigado por entrar no nosso guia de Valorant!")
            os.system("pause")
            exit()

if __name__ == "__main__":
    main()
