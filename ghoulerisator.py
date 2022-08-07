import webbrowser ## import webbrowser library
from time import sleep ## import sleep() method from time for breaks between raws
os = input('type your os(win/mac): ') ## getting information about user's OS for correct programm's work

try:  ## creating try-except-finally construction
    if os == 'win':     
        webbrowser.get(using = 'windows-default').open_new_tab('https://www.youtube.com/watch?v=QKXi08chD2E&t=0s') 
        sleep(9.7)
        for i in range(1000, -15000, -7):
            print(i, '- 7 =', i - 7)
        print("now, you're ghoul")
    elif os == 'mac':
        webbrowser.get(using = 'safari').open_new_tab('https://www.youtube.com/watch?v=QKXi08chD2E&t=0s')
        sleep(9.7)
        for i in range(1000, -15000, -7):
            sleep(0.1)
            print(i, '- 7 =', i - 7)
        print("now, you're ghoul")
    else:
        print('incorrect input')
        print('closing programm...')
        quit()
    
except KeyboardInterrupt:
    print('')
    print('poseur.')

finally:
    print('bye.')


#                   ........;x000000000000000OocoOK000000000000xc:cd00000000OO00Oxclk000000000000dclk00OOOOOOOOOOOOOOOkkkOxdxkkkkkxoldkxxdldxxxxxxxxxxd
#                   .......:dO000000000000000dclOK000000000K00xc:ckK0K0000000000Olcd0K00000000000kcck00O00OOOOOOOOOOOOOkkOkookkkkkkkolxkkkdldxxxxxxxxxd
#                      ..'lddk00000000000000xccx0000000000000xc:ckK0000000000000dco000K0000000000kcck00OOOOOOOOOOOOOOOOOOOOxldOOkkkkxllxkkxloxxxxxxxxxd
#                      .,lllk00000000000000kl:dO000000000000kl:ckK0000000OO0KKOd:ck00000000000kkOklcx000OOOOOO0OOOOOOOOOkOOkolkOkkkkkdclxxxoloxxxxxxxxd
#                     .;;',d0000000000000KOo:lkK0000000000KOl::x0K000000Odx0K0d::d00000000000xdOxxdcd00OOOOOOO0OOOkOOOOOkOkkdcdkkxxkkko:oxdollxxxxxxxxd
#                   ..'...ckO0000000000000xc:d00000000000KOo:;lO0000000xloOKKxc:lk0000000000Odk0odxcoO0OOOOOO00O0OxkOOOkkOOkxclxkxdxkkxc:dxolldxxxxxxxd
#                   ..  .;dxO0O000OkO0000Ol:lOK00000000000dc:cx000000OoclOKkdl:cx0Ok00000O00xx0xcdOllk00OOO0OOOkOOxxOOkddkOOkocdkkodkkdc;cddlllxxxxxxxx
#                       .ldk0OxO0Odd00000d::x000000000OkOxc:;oOK0OO0kl:cx0Oo:::lO0xx0000xokOdkOo:dOd:d00O0OOOOxok0kdxOOxlokOkdclxkooxkxc;;cdolloxxxxxxx
#                      .:ddO0kx00xlxK00Kkl;lkK0000000Oxkkl:;cxKKOdddc::ldkdc:::d0klx000Oocxxx0kc:oOxcck00000OOxcokOdokOOdcokOxlcdkolxkxl:;:lolcldxxxxxd
#                      'ddxKOok0klckK000o::d0000000K0dxOo:::d0K0dclc:::cdxl:::ckOlcx000x::ookKd::lOkc:oO0OO0OOxc:okxcokOkc:okkl:lkdcdkxo:;;:clccoxxxxxd
#                     .lxdO0doOOo:lkK00kc;ckK000000Oookdc::lOK0xc::::::lxo::::lkd:cx00Ol::loO0o::lkkc;ck0O00OOxc::okocdkko::oko:cxd:lxkdc;;;:ccclxxxxxx
#                     ;dcl0kclkdc:lk0OOo:;lOK00000Oolxxc:::d00xc:::::::ddc::::odc::d00d:::cd0kc::ckkl::oO00OO0kl:::odccdkd:;:odc:od::dkxc;;;;:ccldxxxxd
#                    'c'.o0o:loc::lkxdxc;:o0000000dcokl:::ckKOl:::::::cdl:::::ll:::o0Oo::::d0d:::ckkc::lkkkOO0kl:::colclxdc:;col:coc:okxc;;;;;:ccoddxxd
#                   ... .xkc:ccc::lxddd:;:x0OkO00xccxo::::o0Oo::::::::ll:::;;:lc:::o0kc:::;oko:::ckkc:::oookxOOl:::::cc:oxl;;;cl::c::cdxc;;;;;;::lodxxd
#                       ,xd:::::::loldl;;ck0xodOOl:odc:::cx0dc;:::::::cc;;;;;:c::::lkx::::;ldc:::cxxc:::ccclcdko::::::::col::;;:::::;:dxc;;;;;;;:::cdxd
#                       :xl;::::::ccloc;;lO0o:dOd:col::::lOkc:::::::::::;;;;;::::::cxo::::;clc::::oo:::::::::cdo::::::::::c::;;;::::;;ldc;;;;;;;:;;;lxd
#                      .cxc:::::::;;cl:;:lOkc:xkl:ll:::::oko::::::::::::;;;::::::::col::::;:::::::ol::::::::::cl::::::::;:::::;;;;;::;coc;;;;;;;;;;;cdd
#                      .od::::::::;;cc:;:oOd:lkd::c:;::::ddc::::::::::::;;::::::::::cc:::::::::::col:::::::::::::;::::::::::;:;;;;;;:;:c:;;;;;;;;;;;:od
#                      ,xo::::::::;:::;::oko;lxl:::;::::col:::::::::::;;;::::::::::::::::::::::::clc::::::::::;;:;::::::::::;::;;;:;:;;:;;;;;;;;;;;;;ld
#                      ckl::::::::;;::;::odc;clc::;:::::clc:::::::::::;;;:::::::::::::::::::::::::cc::::::::::::::::;:::::::;;:;;;::;;;;;;;;;;;;;;;;;co
#                     .oxc;:::::::;;:::::loc;:c:::;::::::::::::::::::;;;::::::::;;::::::::::::::::::;:::::::::::;:::;::::;::;;::;;;:::;;;;;;;;;;;;;;;:l
#                     ':c:;::::::::;:::::cc:;::::;;:::::::::::::::::;;;:::::;:::,,;::::::::::::::;::::::::::;;::;:::;,;:;;::;;;:;;;:;:;;;;;;;;;;;;;;;;:
#                    .:c::::::::::;::::::::;;:::;;::;::::::::::::;;;;::::;;::;,'';:::::::;::::::;;::::;;;;;:;;:;;:::,,;::::;;;:;;;:;;;:;;;;;;;;;;;;;;;
#                     'c:;:::::::::;::::::::;;:::;::::::::::::::::;,;::::,,;::,..',::;:::::::::::::::;:;;;,,;;;:;,;::,'';;:;;,;;:;;;;;;:;;;;;;;;;;;;;;;
#                    .,,';;;;::::::;;:::::::;:::;;:::::::::::;:::;,;:::;,',;:,'...';:;:::::;;::::::::;;;;;'',;;;,',::;'.,;:;;,';:;;;;;;;;;:;;;;;;;;;;;;
#                   ....,;;:::::::;;;;:::::;:::;;:::::::::;;;::;'';::,'.';,,'....';:;:::::;,;:::::::;;;;;'.',;;,.',;;...,;;;'.,:;;;;;;;;;;;;;;;;;;;;;;
#                    .  .';;;:::::::;;;:::::;:::;:::::;;:::;;::;'.';:,...',........,;;:::::,,;:::::::;;;,;'...',,...,;....;;,'.,;;;;;;;;;;;;;;;;;;;;;;;
#                        .,;;::::::::;::::::;:::;:::::;;;;;,;::,'',;,'..''..........,;::::;'';:::::::;;,,,'....''...','...';,'..,;;,;:;;;;;;;;;;;;;;;;;
#                        .';;:::::::::;:::::;:::;:::::;;;;,';:,'.',,'..''...........,;;:::,'',;;;::::;;,,,'..........'.....''....;;,;;;;;;;;;;;;;;;;;;;
#                         .,;:;;:::::::::::;;;:::::;::;,,'..;,.. ... ...............',;::;,''';;;::::;;,',.............    ..    .;,';;;;;;;;;;;;;;;;;;
#                         ..,:,,;:::::::::;:::::::;;;;,'...';,'''.               ....,;;:;'.'',;,;:;;;;,''....                    ',.';;;;,;;;;;;;;;;;;
#                          .;,..;:;::::::;;::::::::;:;,,'..';;;coo:.''.....  .''.....',,;;..'',,',;;;;;,''...             ....    .'..,;;;,,;;;;;;;;;;;
#                          .,. .;;;:::;;;,;:::;;:::;;,'''..,,,cdOK0Okoc:::lodxko:,...',,;,'''',,'',;;;,'''....                     .'.,;;,',;,,;,;;;;;;
#                         .'.  .,;,;;,.,,,;:;;,,;::;;,'''';;,''';clodxddddxxddoc,'...'',,,;:,',,''',;;,''''.....               .....''',;,',;,,,,;,;;;;
#                         ..   .,'.,;..''';:;,'',;:;,'''':oc',clc;'.';:;;;;;;;;;;;;:;',,,,lo:'',',,',,;;,'','.'..............',;c:'..'',,,',,''',,',;;,
#                              ....,'...',;;,''.',::;',,;lxo;;oxxd:,:odddddddxxxxxxxl,:c;;lxl,',,::;;;:o:';lolc::;;,,,,;;::ccloodl;''''','','.''','.',,
#                              .. .,. .'.';,'''..',:;,,:cdxxocoxxxoodxxxxxxxxxxxxxxxl;lo:;oxo,',;olcccodc;ldddddddoooodddddddddddocc:'''''''.....'...',
#                                 ... ....,'.'....';:,;ldxxxxddxxxxxxxxxxdddddxxxxxdlcdxc:oxo;',cddoodddl:oddddddddddddddddddddddoodl,''''...........,.
#                                      ...';'.'....';;:oxxxxxdxxxxxxxxxdlcclloxdxxxddoxxoldxo;':oxxxxxdxooddddddddddddddddddddddddooo:'''''..........'.
#                                      ..  .',......';cdxxxxxxdxxxxxxdlccccodxxxxxxxxxxxxddxdc;ldxxddxdxdddddddddddoodolloddddddddodo:,'''........  ...
#                                            .,,.....,ldxxxxxxxxdxxxxdoddoodxxxxxdxxxxxxxxxxxdodxddddddddddddddddolclodooooodddddoodo:,''.......     . 
#                                             .;:;'..'cxxxxxxxxxxxxxxxxxdodxxxxxdddddddddxddxddxxddddddddddddddddollllooddlcoddddoodo;''.......        
#                                              .;ol;'.;oxxxxxxxxxxxxxxxxxooxxxxddddddddddddxddxxxdddddddddddddddddddolodddoloddoooooc,''......         
#                                                'lol,'cdxxxxxdxxxxxxxxxdloxxxdxxddddddddxxxdxkxxddxddddddddddddddddooddddddddddoddo:'''''....         
#                                                  .,,',lxxxdxxdddxxxxxxxxxxxxxxxxdddddxxolodxOkdddddddddxxddddddddoooodddddooddodo:,'',''...          
#                                                   ,:;;:dxxdooooddxxxxddxxxxxxxxxddddddxc,;lxxxxdddxxddddddddddddolollldddddddddoc,',;;;,.            
#                                                   ';::;coxxdxxxxxxxxxxxdxxxxxxxxdddddxxl;,,cdxdlcldddddddddddddddddolodddddodooc,',;;,;,.            
#                                                   ',;::;:ddodddddxxdodxdddxxxxddddddddddolclddolodxddddddddddddddddddddddddddoc;',;;..,.             
#                                                   ...;;;;:lodxddxdxdodxddddxxxddddddddddxdddddddxxdddddddddddddddddddddoodddoc,',;;.  ..             
#                                                      .,',;:oxxxxxxddooxxdddxxxdddxxdddxdddddxdddxxxxxxdddddddoooollccloloddl;,',;;'                  
#                                                       ...;;;cdxddxddllxxxdddxxxxxddddddxddxxxddddxxxxxxdddoc:;,,,''';:lcloc,'',;,'.                  
#                                                          .'.,:ldooolcoxxxddxxxxdooooooooooddoloooooooooolc,.........,clc:;'''.',,.                   
#                                                           . .';clddlcoxxxdddddxxdxxdxxdddxxddddddddddddoc,..... ...,::;'''';' .'.                    
#                                                               ',';loooddxddddxddxxdddxxddxxxxxxdxdddddol:'.......,;;'...'.',.  .                     
#                                                                ...,:coddxddddxdddddddddoccccccccloddxdl:,..';:c:,,''...'. .'                         
#                                                                 ..'',,;coxxxddxddddddddol::::::cloddddoc::cooc:,'....''.  ..                         
#                                                                   .','.',:cloddddddddddxdddddddddddddddooooc;''.....''.                              
#                                                                   .''''.''',,:coddddddddddddddddddddooddoc,''''''...'.                               
#                                                                    .''''.'',,'',:coddxdddddddddddddoccl:,'.'''''...'..                               
#                                                                     .....''''''''',;:loddddddddddlll;,''''''''........                               
#                                                                         .....''''''''',;:ccloool:,,'..........    ...                                
#                                                                              ....''''''...............                                               
#code by                                                                                                                                                      
#        ___          _ _____ 
# _ __  / _ \ ___  __| |___  |
#| '_ \| | | / __|/ _` |  / / 
#| |_) | |_| \__ \ (_| | / /  
#| .__/ \___/|___/\__,_|/_/   
#|_|                                                                                                                                                                             
#
#
#illustrating ascii graphics: https://www.ascii-art-generator.org                                                                                                                             
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
