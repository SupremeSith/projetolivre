class Agente():
    def Listar_Habilidades_1():
        print ("Todos os Agentes tem caracteristicas em comum, todos podem andar e pular pelo mapa e se estiverem com dinheiro poderão comprar armas de diversos tipos")



class Jett(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Jett são:\n1- Q - CORRENTE ASCENDENTE \n INSTANTANEAMENTE impele Jett bem alto no ar. \n\n 2- E - BRISA DE IMPULSO\n ATIVE para preparar uma rajada de vento por tempo limitado. REPITA a habilidade para lançar Jett na direção do movimento atual dela. Se estiver parada, Jett será lançada para a frente. A carga de Brisa de Impulso é redefinida a cada dois abates.\n\n 3- C - ERUPÇÃO DAS BRUMAS\n Lança INSTANTANEAMENTE um projétil que se expande numa breve nuvem que obscurece a visão ao bater numa superfície. SEGURE o botão da habilidade para curvar a fumaça na direção da sua mira.\n\n 4-  X TORMENTA DE AÇO \n EQUIPE um conjunto de facas de arremesso altamente precisas. DISPARE para lançar uma única faca contra o alvo. As facas são recarregadas ao matar um oponente. Use o DISPARO ALTERNATIVO para jogar todas as facas restantes contra o alvo, porém elas não são recarregadas ao matar um oponente."
        print (a)
        
class Raze(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Raze são:\n1- Q - CARGA DE EXPLOSIVOS \n INSTANTANEAMENTE joga uma Carga de Explosivos que gruda em superfícies. REUSE a habilidade depois de instalar para detonar, causando dano e movendo tudo que for atingido. Raze não sofre dano ao ser atingida pelo efeito desta habilidade, mas ainda pode sofrer dano de queda se for arremessada para longe. \n\n E - CARTUCHOS DE TINTA \n EQUIPE uma granada múltipla. DISPARE para jogar a granada, que causa dano e cria submunições, cada uma causando dano a qualquer um que estiver no alcance. Use o DISPARO ALTERNATIVO para arremessar a curta distância. A carga dos Cartuchos de Tinta é redefinida a cada dois abates.\n\n C - BUMBA \n\n EQUIPE um Bumba. DISPARE para lançar o robô, que avança em linha reta no chão, ricocheteando nas paredes. O Bumba trava ao detectar inimigos no cone frontal e os persegue, explodindo e causando muito dano se alcançá-los.\n\n X - ESTRAGA-PRAZERES\n EQUIPE um lança-mísseis. DISPARE um foguete que causa dano devastador em área ao fazer contato com qualquer coisa."
        print (a)

class Sage(Agente):
    def mostrar_habilidade():
        a = "As habilidades de Sage são:\n1- Q - ORBE DE LENTIDÃO (O orbe detona ao pousar, criando um campo duradouro que desacelera os jogadores dentro dele.)\n\n 2- E - ORBE CURATIVO (Use enquanto Sage estiver ferida para ativar uma autocura ao longo do tempo.)"
        print (a)

class Cypher(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Cypher são: \n1- Q - JAULA CIBERNÉTICA\n INSTANTANEAMENTE joga a jaula cibernética diante de Cypher. Ative para criar uma zona que bloqueia a visão e reduz a velocidade de inimigos que passarem por ela.\n\n 2- E CÂMERA DE VIGILÂNCIA \n EQUIPE uma Câmera de Vigilância. DISPARE para colocar a câmera no local-alvo. REPITA a habilidade para controlar a visão da câmera. Enquanto controla a câmera, DISPARE para lançar um dardo marcador. O dardo revelará a localização de qualquer jogador atingido. A câmera pode ser recuperada e REPOSICIONADA.\n\n 3- C - FIO-ARMADILHA \n EQUIPE um fio-armadilha. DISPARE para instalar um fio acionador oculto e destrutível no local-alvo, criando uma linha entre o local e a parede oposta. Jogadores inimigos que passarem por um fio e não destruírem o dispositivo a tempo ficarão imobilizados, revelados e estonteados depois de um breve intervalo. A habilidade pode ser recolhida para ser REPOSICIONADA.\n\n 4- X - ASSALTO NEURAL \n Use INSTANTANEAMENTE num jogador inimigo morto na sua mira para revelar a localização de todos os jogadores inimigos ainda vivos."
        print (a)

class Sova(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Sova são: \n1- Q - FLECHA DE CHOQUE \n EQUIPE um arco com uma flecha de choque. DISPARE para lançar a flecha, que explode com o impacto causando dano aos jogadores próximos. SEGURE O DISPARO para estender o alcance do projétil. Use o DISPARO ALTERNATIVO para adicionar até dois ricochetes à flecha.\n\n 2 - E FLECHA RASTREADORA\n EQUIPE um arco com uma flecha de reconhecimento. DISPARE para lançar a flecha, que é ativada mediante impacto e Revela a localização de quaisquer inimigos próximos da linha de visão. Inimigos podem destruí-la. SEGURE O DISPARO para estender o alcance do projétil. Use o DISPARO ALTERNATIVO para adicionar até dois ricochetes à flecha.\n\n 3- C - DRONE CORUJA \n EQUIPE um drone coruja. DISPARE para acionar e pilotar o drone. Enquanto pilota o drone, DISPARE para atirar um dardo marcador. O dardo revelará a localização de qualquer jogador atingido. Inimigos podem destruir o Drone Coruja.\n\n 4 - X - FÚRIA DO CAÇADOR \n EQUIPE um arco com três disparos de longo alcance que perfuram paredes. DISPARE para atirar um raio de energia diante de Sova, causando dano e revelando a localização dos inimigos que estiverem na linha. A habilidade pode ser REPETIDA mais duas vezes enquanto o cronômetro de habilidade estiver ativo."
        print (a)
class Brimtone(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Brimstone são: \n1- Q - INCENDIÁRIO\n EQUIPE um lançador de granadas incendiárias. DISPARE para lançar uma granada que detona no chão, gerando uma zona de fogo que causa dano aos jogadores dentro dela.\n\n2 - E - FUMAÇA CELESTE\n EQUIPE um mapa tático. DISPARE para marcar os locais onde as nuvens de fumaça de Brimstone pousarão. Use o DISPARO ALTERNATIVO para confirmar, lançando nuvens de fumaça de longa duração que bloqueiam a visão na área selecionada.\n\n3- C - SINALIZADOR ESTIMULANTE\n EQUIPE um sinalizador estimulante. DISPARE para jogar o sinalizador diante de Brimstone. Ao pousar, o sinalizador criará um campo que concede Tiro Rápido aos jogadores.\n\n4- X - ATAQUE ORBITAL\n EQUIPE um mapa tático. DISPARE para lançar um ataque prolongado de laser orbital no local selecionado, causando muito dano ao longo do tempo aos jogadores na área selecionada."
        print (a)
class Omen(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Omen são: \n1- Q - PARANOIA\n INSTANTANEAMENTE emite um projétil sombrio adiante, reduzindo brevemente o alcance de visão dos jogadores tocados. O projétil atravessa paredes.\n\n 2- E - MANTO SOMBRIO\n EQUIPE um orbe sombrio e entre em um universo distorcido para posicionar os orbes. PRESSIONE o botão de habilidade para lançar o orbe no local marcado, criando uma esfera de sombra duradoura que bloqueia a visão. SEGURE O DISPARO enquanto mira para afastar o marcador. SEGURE O DISPARO ALTERNATIVO enquanto mira para aproximar o marcador. PRESSIONE RECARREGAR para alternar para a visão de mira normal.\n\n 3- C - PASSOS TENEBROSOS\n EQUIPE uma habilidade de passos sombrios e olhe o indicador de alcance. DISPARE para começar uma breve canalização e, então, teleporte-se para o local marcado.\n\n4 - X - SALTO DAS SOMBRAS\n EQUIPE um mapa tático. DISPARE para começar a se teleportar ao local selecionado. Enquanto se teleporta, Omen aparecerá como um Vulto que pode ser destruído por qualquer inimigo para cancelar o teleporte."
        print (a)

class Phoenix(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Phoenix são:\n1 - Q - BOLA CURVA\n EQUIPE uma bola curva. DISPARE para lançar a bola, que explode causando dano aos inimigos próximos. A habilidade pode ser curvada na direção da sua mira.\n\n2- E - PAREDE FLAMEJANTE\n EQUIPE uma parede flamejante. DISPARE para criar uma parede de fogo que bloqueia a visão e causa dano a quem passar por ela. A habilidade pode ser curvada enquanto mira.\n\n3- C - CAMINHADA DIVINA\n EQUIPE uma caminhada divina. DISPARE para ativar a habilidade, fazendo Phoenix se transformar em uma forma imaterial temporária que o deixa invulnerável. Enquanto ativo, você pode posicionar um marcador de ressurgimento. Se Phoenix for derrotado, ou se a habilidade for reativada, ele ressurgirá no local do marcador.\n\n4- X - RAIOS SOLARES\n INSTANTANEAMENTE lança três esferas de fogo consecutivas que explodem causando dano em uma ampla área. Você pode escolher onde cada esfera será lançada antes do disparo."
        print (a)

class Viper(Agente):
    def mostrar_habilidade():
        a = "as habilidades especiais de Viper são:\n1 - Q - NUVEM VENENOSA/n EQUIPE um emissor de gás. DISPARE para jogar o emissor, que persiste até o fim da rodada. REPITA para criar uma nuvem de gás tóxico que drena combustível. A habilidade pode ser REPETIDA mais de uma vez e pode ser recolhida para ser REPOSICIONADA.\n\n E - CORTUNA TÓXICA \nEQUIPE um lançador de emissores de gás. DISPARE para lançar uma longa linha de emissores de gás. REPITA a habilidade para criar uma parede alta de gás tóxico que drena combustível. A habilidade pode ser REPETIDA mais de uma vez.\n\n C - VENENO DE COBRA\n EQUIPE um lançador químico. DISPARE para lançar um cilindro que se rompe ao atingir o chão, gerando uma zona química duradoura que causa dano e reduz a velocidade dos inimigos.\n\n X - POÇO PEÇONHENTO\n EQUIPE um borrifador químico. DISPARE para borrifar uma nuvem química em todas as direções ao redor de Viper, criando uma grande nuvem que reduz o alcance de visão e a Vida máxima dos jogadores dentro dela. "
        print (a)

class Breach(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Breach são:\n1 - Q - ESTOPIM\n EQUIPE uma carga cegante. DISPARE a carga para armar um jato de ação rápida pela parede. A carga é detonada, cegando todos os jogadores que estiverem olhando para ela.\n\n2- E - FALHA TECTÔNICA\n EQUIPE um impacto sísmico. SEGURE O DISPARO para aumentar a distância. SOLTE para iniciar o terremoto, estonteando todos os jogadores na zona e numa linha reta até a zona.\n\n3- C - PÓS-CHOQUE\nEQUIPE uma carga de fusão. DISPARE a carga para armar um jato de ação lenta pela parede. O jato causa muito dano a todos que estiverem na área de efeito.\n\n4- X - ONDA TROVEJANTE\n EQUIPE uma carga sísmica. Dispare para lançar um terremoto em cascata por todo o terreno num grande cone. O terremoto estonteia e derruba todos que estiverem na área de efeito."
        print (a)

class Reyna(Agente):
    def mostrar_habilidade():
        a = "As habilidades da Reyna são: \n 1- Q - DEVORAR \n Inimigos abatidos por Reyna deixam Orbes de Alma que duram 3s. INSTANTANEAMENTE consome um Orbe de Alma próximo, curando-se de forma rápida por um curto período. A quantidade de Vida concedida por esta habilidade que ultrapassar 100 decairá ao longo do tempo. Se a habilidade IMPERATRIZ estiver ativa, esta habilidade será conjurada automaticamente e não consumirá o orbe. \n 2- E - DISPENSAR \n INSTANTANEAMENTE consome um Orbe de Alma próximo, ficando inatingível por um curto período. Também se torna invisível se a habilidade IMPERATRIZ estiver ativa. \n 3- C - OLHAR VORAZ \n EQUIPE um olho etéreo e destrutível. ATIVE para lançá-lo adiante a uma curta distância. O olho deixará com visão turva todos os inimigos que olharem para ele. \n 4- X - IMPERATRIZ \n INSTANTANEAMENTE entra em estado de frenesi, aumentando de forma drástica as velocidades de disparo, equipamento e recarga de munição. Renova a duração ao fazer um abate."
        print (a)

class Killjoy(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Killjoy são:\n1- Q - NANOSSENTRIELHAS\n EQUIPE uma Nanossentinela. DISPARE para implantar uma sentinela que detecta inimigos na linha de visão e os atinge com uma rajada de dardos. SEGURE a habilidade para curvar a trajetória dos dardos.\n\n E - BLOQUEIO CRIPTOGRAFADO\n EQUIPE um Bloqueio Criptografado. DISPARE para implantar uma barreira de energia que se estende e bloqueia o progresso dos inimigos. SEGURE a habilidade para curvar a barreira enquanto a implanta.\n\n C - REVELADOR\n EQUIPE um Revelador. DISPARE para lançar o dispositivo que se prende a uma superfície. REUSE a habilidade para ativar o dispositivo e emitir um pulso que revela a localização de todos os inimigos na área.\n\n X - MÁXIMA / MÍNIMA\n EQUIPE uma bomba de ataque. DISPARE para lançar a bomba, que se fixa em superfícies. REUSE a habilidade para alternar entre duas opções de explosão: uma que causa dano maior ou outra que dispara várias explosões menores."
        print (a)

class Skye(Agente): 
    def mostrar_habilidade():
        a = "As habilidades Especiais de Skye são:\n1- Q - LUZ GUIA\n EQUIPE um dispositivo de luz guia. DISPARE para lançá-lo, causando uma explosão que cura aliados próximos. SEGURE a habilidade para mirar e escolher a distância do lançamento.\n\n2-  E - INVESTIDA SELVAGEM\n EQUIPE uma investida selvagem. DISPARE para ativar a investida, que causa dano e atordoa os inimigos que estiverem no caminho.\n\n3- C - PREDADOR TERRESTRE\n EQUIPE um predador terrestre. DISPARE para lançá-lo, criando uma sentinela que detecta inimigos na área e dispara projéteis que os atordoam. SEGURE a habilidade para ajustar a distância do lançamento.\n\n4- X - DESPERTAR SELVAGEM\n ATIVE para invocar um lobo selvagem que avança rapidamente e revela inimigos próximos. REUSE a habilidade para controlar o lobo, mordendo e atordoando inimigos atingidos. Enquanto controla o lobo, você assume uma forma imaterial."
        print (a)

class Yoru(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Yoru são:\n1- Q - FENDA DIMENSIONAL\n EQUIPE uma Fenda Dimensional. DISPARE para lançar a fenda, que cria portais ligando dois locais. Ao entrar na fenda, você é teleportado para o outro lado.\n\n2 - E - PASSO SOMBRA\n EQUIPE um dispositivo de passo sombra. DISPARE para lançá-lo, criando uma entrada em um local. Use a habilidade novamente para criar uma saída em um local diferente, permitindo um rápido deslocamento entre eles.\n\n3- C - CHICOTE DIMENSIONAL\n EQUIPE um chicote dimensional. DISPARE para lançar o chicote, que se expande e puxa todos os inimigos próximos na direção dele. REUSE a habilidade para puxar o chicote de volta.\n\n4- X - FRAGMENTAÇÃO DIMENSIONAL\n ATIVE para entrar em uma dimensão paralela, tornando-se invisível e imune a dano. Enquanto nessa dimensão, você pode ativar a habilidade novamente para retornar à sua posição original, causando uma explosão que cega os inimigos próximos."
        print (a)

class Astra(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Astra são:\n1- Q - PULSO NOVA\n Posicione Estrelas na Forma Astral (X) ATIVE uma Estrela para detonar um Pulso Nova. O Pulso Nova carrega brevemente e depois estoura, causando concussão a todos os jogadores na área.\n\n2- E - NEBULOSA\n Posicione Estrelas na Forma Astral (X). ATIVE uma Estrela para transformá-la em uma Nebulosa (fumaça). USE uma Estrela para dissipá-la, retornando a Estrela para ser posicionada em um novo local após um período. Dissipar forma brevemente uma Nebulosa falsa na localização da Estrela antes de retornar.\n3- C - POÇO GRAVITACIONAL\nPosicione Estrelas na Forma Astral (X) ATIVE uma Estrela para formar um Poço Gravitacional. Jogadores na área são puxados em direção ao centro antes de ele explodir, deixando frágeis todos que ainda estão presos no centro.\n\n4 - X - FORMA ASTRAL / DIVISA CÓSMICA\n ATIVE para entrar na Forma Astral, em que você pode posicionar Estrelas com o DISPARO. As Estrelas podem ser reativadas depois para serem transformadas em Pulso Nova, Nebulosa ou Poço Gravitacional. Quando Divisa Cósmica estiver carregada, use o DISPARO ALTERNATIVO na Forma Astral para começar a mirar e, depois, o DISPARO para escolher dois locais. Uma Divisa Cósmica infinita surge e conecta os pontos selecionados. A Divisa Cósmica bloqueia disparos e abafa muito o som."    
        print (a)

class Kayo(Agente):
    def mostrar_habilidade():
        a = "As habilidades Especiais de Kay/o são:\n1- Q - GRANADA/CLARÃO\n EQUIPE uma granada de clarão. DISPARE para jogá-la por cima. Use o DISPARO ALTERNATIVO para arremessar a curta distância uma versão mais fraca que explode mais rápido. A granada de clarão explode após um curto período, Cegando qualquer um que estiver na linha de visão.\n\n2- E - PONTO/ZERO\n EQUIPE uma lâmina de supressão. DISPARE para lançar. A lâmina se fixa à primeira superfície que atingir e explode, Suprimindo qualquer um que estiver dentro do raio da explosão. Inimigos podem destruir a lâmina.\n3- C - FRAG/MENTO\nEQUIPE um fragmento explosivo. DISPARE para lançá-lo. O fragmento se fixa ao chão e explode várias vezes, causando dano quase letal no centro de cada explosão.\n\n X - ANULAR/CMD\n INSTANTANEAMENTE sobrecarrega com energia de Radianita polarizada que emite grandes pulsos energéticos em um raio enorme a partir de onde KAY/O estiver. Inimigos atingidos pelos pulsos são Suprimidos por um curto período. Enquanto estiver sobrecarregado, KAY/O recebe Estimulante de Combate e pode ser reestabilizado se for abatido."
        print (a)

class Neon(Agente):
    def mostrar_habilidade():
        a = "As habilidades da Neon são: \n1- Q - RICOCHETE ELÉTRICO \n INSTANTANEAMENTE arremessa um raio de energia que ricocheteia uma vez. Ao atingir cada superfície, o raio eletrifica o chão abaixo dele com uma explosão. \n 2- E - EQUIPAMENTO VOLTAICO \n INSTANTANEAMENTE canaliza o poder de Neon para receber velocidade aumentada. Ao atingir a carga máxima, use o DISPARO ALTERNATIVO para acionar um deslize elétrico. O carregamento é redefinido a cada dois abates. \n 3- C - VIA EXPRESSA \n DISPARE duas linhas de energia no chão à frente. As linhas se estendem por uma curta distância ou até atingirem uma superfície. Elas se tornam paredes de eletricidade estática que bloqueiam a visão e causam dano aos inimigos que as atravessarem. \n 4- X - SOBRECARGA \n Neon libera todo o seu poder e velocidade por um curto período. DISPARE para canalizar isso em um raio elétrico mortal com alta precisão de movimento. A duração é redefinida com cada abate."
        print (a)

class Chamber(Agente):
    def mostrar_habilidade():
        a = "As habilidades do Chamber são: \n1- Q - CAÇADOR DE CABEÇAS \n ATIVE para equipar uma pistola pesada. Use o DISPARO ALTERNATIVO com a pistola equipada para mirar. \n 2- E - RENDEZVOUS \n EQUIPE uma âncora de teleporte. DISPARE para posicioná-la no chão. Enquanto estiver no chão e dentro do alcance da âncora, REATIVE para teleportar rapidamente até a âncora. A âncora pode ser recuperada para ser REPOSICIONADA. \n 3- C - MARCA REGISTRADA \n EQUIPE uma armadilha que busca por inimigos. DISPARE para posicioná-la no chão. Quando um inimigo visível entra no alcance, a armadilha inicia uma contagem regressiva e desestabiliza o terreno ao redor, criando um campo duradouro que Desacelera os jogadores dentro dele. A armadilha pode ser recuperada para ser REPOSICIONADA. \n 4- X - TOUR DE FORCE \n ATIVE para invocar um poderoso fuzil de precisão personalizado que abate um inimigo com qualquer acerto na parte superior do corpo. Use o DISPARO ALTERNATIVO para mirar. Abater um inimigo cria um campo duradouro que Desacelera os jogadores dentro dele."
        print (a)


class Deadlock(Agente):
    def mostrar_habilidade():
        a = "As habilidades da Deadlock são: \n1- Q - SENSOR SÔNICO \n EQUIPE um Sensor Sônico. DISPARE para posicionar. O sensor monitora os sons dos inimigos em uma área. Causa concussão na área se sons de passos, disparos ou qualquer barulho significativo forem detectados. \n 2- E - MALHA DE BARREIRA \n EQUIPE um disco de Malha de Barreira. DISPARE para lançar à frente. Ao atingir o chão, o disco gera barreiras a partir do ponto de origem que bloqueiam a movimentação de personagens. \n 3- C - GRAVNET \n EQUIPE uma granada GravNet. DISPARE para lançar. Use o DISPARO ALTERNATIVO para arremessar a curta distância. A GravNet detona ao atingir o chão, forçando inimigos pegos por ela a agacharem e moverem-se lentamente. \n 4- X - ANIQUILAÇÃO \n EQUIPE um Acelerador de Nanofios. DISPARE para liberar um pulso de nanofios que captura o primeiro inimigo que encontrar. O inimigo encasulado é puxado por uma trilha de nanofios e abatido se chegar ao final da trilha, a não ser que seja libertado. O casulo de nanofios é destrutível."
        print (a)


class Gekko(Agente):
    def mostrar_habilidade():
        a = "As habilidades do Gekko são: \n1- Q - WINGMAN \n EQUIPE Wingman. DISPARE para enviá-lo para encontrar inimigos. Wingman lança uma forte explosão na direção do primeiro inimigo que vê. Use o DISPARO ALTERNATIVO na direção de um ponto ou Spike plantada para que Wingman plante ou desarme a Spike. Para plantar, Gekko deve estar com a Spike no inventário. Quando Wingman expira, ele se transforma em um glóbulo inativo. INTERAJA para recuperar o glóbulo e ganhar outra carga de Wingman após um curto período. \n 2- E - DIZZY \n EQUIPE Dizzy. DISPARE para enviá-la voando pelo ar. Dizzy avança e solta explosões de plasma nos inimigos em sua linha de visão. Os inimigos atingidos pelo plasma ficam cegos. Ao expirar, Dizzy se transforma em um glóbulo inativo. INTERAJA para recuperar o glóbulo e ganhar outra carga de Dizzy após um curto período. \n 3- C - MOSH PIT \n EQUIPE Mosh. DISPARE para lançá-lo como uma granada. Use o DISPARO ALTERNATIVO para lançar por baixo. Ao atingir uma superfície, Mosh se duplica em uma grande área e, depois de uns instantes, explode. \n 4- E - THRASH \n EQUIPE Thrash. DISPARE para se conectar à mente dela e guiá-la pelo território inimigo. ATIVE para avançar e explodir, detendo qualquer inimigo em um pequeno raio. Ao expirar, Thrash se transforma em um glóbulo inativo. INTERAJA para recuperar o glóbulo e ganhar outra carga de Thrash após um curto período. Thrash pode ser recuperada uma vez."
        print (a)



class Mapa():
    def Mapas():
        print ("Os mapas tem entre dois e três bomb sides, onde uma equipe é atacante e tem o objetivo de fazer o plant da spike, enquanto a outra equipe protege os bomb sides e remove a spike se for implantada.")


        
class Bind(Mapa):
    def descrever_mapa():
        c = "Mapa Bind \n 2 bomb sites divididos entre o A e o B \n O mapa representa um deserto que é separado por dois portais"
        print (c)
    
class Haven(Mapa):
    def descrever_mapa():
        c = "Mapa Haven \n 3 bomb sites divididos entre o A, B e C \n O mapa representa uma cidade chinesa"
        print (c)
   
class Split(Mapa):
    def descrever_mapa():
        c = "Mapa Split \n 2 bomb sites divididos entre o A e o B \n O mapa representa um laboratório"
        print (c)
   
class Ascent(Mapa):
    def descrever_mapa():
        c = "Mapa Ascent \n 2 bomb sites divididos entre o A e o B \n O mapa representa uma cidade italiana"
        print (c)
                
class Icebox(Mapa):
    def descrever_mapa():
        c = "Mapa Icebox \n 2 bomb sites divididos entre o A e o B \n O mapa representa um depósito de radianita e dominada pela kingdom"
        print (c)
    
class Breeze(Mapa):
    def descrever_mapa():
        c = "Mapa Breeze \n 2 bomb sites divididos entre o A e o B \n O mapa representa uma ilha tropical"
        print (c)
    
class Fracture(Mapa):
    def descrever_mapa():
        c = "Mapa Fracture \n 2 bomb sites divididos entre o A e o B \n O mapa representa uma cidade futurista"
        print (c)
    
class Pearl(Mapa):
    def descrever_mapa():
        c = "Mapa Pearl \n 2 bomb sites divididos entre o A e o B \n O mapa representa uma cidade portuguesa"
        print (c)

class Lotus(Mapa):
    def descrever_mapa():
        c = "Mapa Lotus \n 2 bomb sites divididos entre o A e o B \n O mapa representa uma cidade perdida"
        print (c)
            
