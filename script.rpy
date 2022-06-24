﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")

# 여기에서부터 게임이 시작합니다.
label start:
    scene bg_topfloor with dissolve
    centered "어째서, 살아가는가.{p}어떻게, 살아가는가.{p}묻던 이들이여."
    centered "이것은 내가 내쉬는 마지막 단락이오, 언어이니.{p}한 때 함께하였던. 화살 돌린 이들이여.{p}꺼져가는 불씨를 다시금 지펴낼 기름더미를 선물하나니.{p}낙향으로의 달음박질은 아직 멈추지 않았음이라."
    "내려다 보았다.{w} 기숙사동 아래 벤치. {w}나무. {w}그리고. {w}이름 모를 돌로 만들어진 바닥."
    "여러 일들이 있었다."
    "고통이 있었고, 그에 수반되는 기쁨이 있었다. {w}그리고. {w}염원했던 것이. {w}무엇을 대가로 내놓더라도 이루고 싶었던 것이. {w}있었다."
    "먼 동이 터오고 있다. {w}곧 잠에서 깨어난 아이들이 쏟아져 나올 것이다."
    "펜스를 밟고 올라섰다."
    scene bg_topfloor2 with dissolve
    "몸이 조금이라도 기울어진다면 곧바로 균형을 잃고 추락하게 될 것이다."
    "흐드러지게 펼쳐진 별무리가 햇빛에 밀려 힘을 잃어가고 있다."
    narr "(슬슬... {w}시간인가.)"
    $SoundPlayer("broadcast.wav", 1.5)
    "이어폰을 꼈다. {w}\'소음\'이 차단되며 노래소리가 주변을 가득히 채워나갔다."
    play music wind
    scene fall_1 with dissolve
    narr "(죽음, 이라.)"
    scene fall_2 with dissolve
    narr "(그러고보니 딱히... {w}진지하게 생각해 본 적이 없었던가...)"
    scene fall_3 with dissolve
    narr "(이제... {w}어떻게 되려나.)"
    window hide
    $ShowImage(4, 11)
    play second kick
    scene fall_10:
        blur 15.0
    with pixellate
    narr "큭...!"
    "칼로 에는 듯한 새벽 바람이 불어닥친다. {w}그럼에도 추위는 느껴지지 않았다."
    "흐려진 시야 너머로 열기가 온 몸을 감싸 안는다. {w}머리께에서 뜨듯미지근한 웅덩이가 느껴졌다."
    narr "하하... {w}하하하하하!!! {w}이것도 한 번... {w}무마해 보라지... {w}아무리 그래도... {w}사람 목숨의 무게는... {w}경우가 다르다고..."
    "끝났다. {w}이제, 모든 것을 바꿀 수 있다. {w}승자는. {w}{i}우리다.{/i}"
    stop music fadeout 3.0
    scene bg_black with eye_close
    $renpy.pause(7.0)
    nvlnarr "제게 있어 행복이란 것은 그러한 것입니다.{p}보이지도 않고, 느껴지지도 않는 헛된 망상.{p}죄송합니다. 제가 할 수 있는 것은 여기까지입니다." with dissolve
    nvlnarr "은설이 형님.{p}둘도 없는 우리 형님.{p}다른 누구보다도 나를 먼저 챙겨줬던 우리 멋진 형님.{p}당신이 계셨습니다."
    nvlnarr "어느날, 형님께서는 제게 말씀하셨습니다.{p}미루었던 질문에 대한 대답을 이제서는 할 수 있을 성싶습니다.{p}저로부터 말미암아 덩그러니 남겨진 과분한 짐.{p}누구에게도 미루지 않겠습니다.{p}이 손으로 희생의 크기를 정해야 한다면.{p}판을 바꾸어 대상을 다시 정의하겠습니다."
    nvlnarr "연호.{p}약해빠진 절 대신하여 선봉에 서 준.{p}제 든든한 오른팔이었던 당신이 계셨습니다."
    nvlnarr "천율.{p}가족보다 가까이에 서 묵묵히 함께하며 숱한 고통과 괴로움, 기쁨을 함께 나누었던.{p}지칠 때마다 가만히 옆에 서 보듬어주던 당신이 계셨습니다."
    play sound paper
    nvl clear
    nvlnarr "고대 그리스 신화에서 가로되.{p}인류에게 허락되지 않은 상자가 열리며 세상에 퍼진 갖은 부정에서 끝내 뛰쳐나가지 못한 채 남은 것은 희망이었다 합니다."
    nvlnarr "희망이 남았기에, 인류는 지금껏 있어왔던 수 차례의 재앙과 번민 속에서도 끝끝내 살아남을 수 있었다 합니다."
    nvlnarr "그러나, 기약없는. 믿음 없는 희망은 위장된 절망에 불과하기에.{p}저희는 꺾일 수 밖에 없었습니다. 분열될 수 밖에 없었습니다."
    nvlnarr "부탁드리겠습니다.{p}청정한 눈으로 바라보아 주십시오.{p}세상은 아직 살 만한 곳이란 것을 눈 감은 이들에게. 무력에 잠식된 이들에게 알려주십시오."
    nvlnarr "사라지는 것은 저 혼자로 충분하니.{p}더 이상 외면하지 말아 주십시오.{p}이렇게, 부탁드리겠습니다."
    hide window
    nvl clear
    play sound wrinkle
    "종이를 구겼다. {w}분이 풀리지 않았다."
    "눈 앞에 펼쳐진 현실을 외면하려 해도. {w}사실이 거짓으로 바뀌는 일은 일어나지 않았다."
    "처음으로 만날 날부터. {w}지금까지. {w}아무것도 하지 못하는 무능한인 채로."
    "또 다시. {w}그들이 나로부터 소중한 것을 빼앗아가는 것을 방관하고 말았다."
    $SoundPlayer("walk_slow.ogg", 2.0)
    "눈을 뜨고 싶지 않다. {w}내 이상이. {w}바램이 만들어낸  환상으로부터. {w}벗어나고 싶지 않았다."
    chunyul "(그렇지만... {w}직시해야만 하겠지. {w}도피는 미봉책일 뿐, 결코 사태를 해결할 수 없으니까.)"
    scene bg_binso 
    show ginsetsu_cry at center
    with eye_open
    chunyul "누나..."
    "강인한 사람이었다. {w}우리 앞에서 한 번도 싫은소리. {w}약한 소리 내지 않을 정도로."
    "그랬던 누나가 멍하니 천장만을 바라본 채 벽에 기대 앉아있었다.{p}알아들을 수 없을 정도로 작은 목소리를 흘려내며 달싹이는 입술. {w}눈가에는 눈물자국이 선명히 남아있다."    
    chunyul "누나...?"
    ginsetsu "......."
    "어깨에 살짝. {w}손을 얹었다."
    "할로겐 전등으로 한껏 달구어진 후덥지근한 공기를 뚫고 손이 거대한 열기와 마주했다."
    chunyul "(뜨거워... {w}체온이 무슨...)"
    ginsetsu "......."
    "살짝. {w}조심스럽게. {w}툭, 툭, 하고 양 어깨를 두드렸다."
    ginsetsu "어?"
    chunyul "누나. {w}나왔어."
    $FaceChange("ginsetsu_bit", 1.0, .5, "ginsetsu_cry")
    "재빨리 눈물자국을 닦아낸 누나는 애써 미소지어 보였다."
    ginsetsu "학교는 어쩌고?"
    chunyul "몰래 나왔어."
    ginsetsu "괜찮은 거야?"
    chunyul "아마도."
    "말 한 마디 한 마디가 조심스러웠다."
    "내가 그 아이와 알고 지냈던 것은 길게 잡아도 2년 반. {w}\'가족\'인 은설이 누나가 느끼고 있을 감정을 헤아릴 수 있다 말하는 것은 오만이자 무례에 불과하다."
    ginsetsu "밥... {w}밥 먹었니?"
    chunyul "응. 먹었-{w=.3}{nw}"
    $SoundPlayer("growl.wav", 2.0)
    chunyul "......."
    ginsetsu "잠깐만 기다려. {w}금방 차려줄게."
    chunyul "...고마워."
    scene bg_binso2 with Fade(2.0, 4.0, 2.0)
    chunyul "꽤 늦어버렸네..."
    ginsetsu "들어가 봐야 하는 거 아냐?"
    chunyul "지금 들어가봤자 벌점 받는 거야 못 피할 거고... {w}내가 없는 편이 나을 거야. {w}아마."
    ginsetsu "역시... {w}또?"
    chunyul "응... {w}그렇지."
    chunyul "이딴 걸 벌써 경험하고 싶진 않았는데 말이야..."
    ginsetsu "어디 갈 곳은 있어?"
    chunyul "집 대신 쓰는 컨테이너 있어. {w}거기 가면 돼."
    ginsetsu "여기랑 정반대잖아. {w}이미 버스도 끊겼는데 어떻게 가게?"
    chunyul "아까 타고 온 자전거 있어."
    ginsetsu "이 한밤중에 다니는 사람 하나 없는 컴컴한 길을 가겠다고?"
    chunyul "별 수 없잖아. {w}미성년자니까 여관방에 갈 수도 없는 노릇이고."
    "불현듯, 머리 속에 스쳐지나가는 것은. {w}떠올리고 싶지 않은 한 남자에 대한 기억."
    ginsetsu "자고 가는 편이 안 낫겠어?"
    chunyul "뭐?"
    ginsetsu "괜히 억지부리지 말고 얌전히 내 말 들어. {w}갔다가 사고라도 나면 그 애를 볼 면목이 없잖아."
    "내뱉으려던 말을 황급히 주워담았다. {w}눈동자가 마주쳤기 때문이었다."
    "깊게 내려앉은 눈그늘. {w}옷소매로 훔쳐냈음에도 채 지워지지 않은 말라붙은 눈물자국.{p}그 너머에 있는 것을 숨기고자 거짓으로 조각된 표정."
    "2년이라는 시간 동안 주어진 상황을 극복하기 위해서. {w}극복할 수 없다면, 적응하기 위해서 길러진 소양.{p}그 덕분에 알아차릴 수 있었다. {w}잠깐의 스침. {w}평소의 누나였더라면 충분히 감추고도 남았을 것이다. {w}명백한 동요."
    "평소라면 나 역시 조작된 감정의 가면을 쓴 채로 받아냈을 것이다. {w}웃음. {w}장난스런 힐난. {w}으로 대꾸할 수 있었을 것이다."
    ginsetsu "부탁할게. {w}느낌이 안 좋아서 그래..."
    chunyul "알았어. {w}어차피 지금까지 쌓인 게 있으니까 퇴소는 확실하고... {w}오늘은 여기서 자고 날이 밝는 대로 갈게. {w}그럼 됐지?"
    ginsetsu "응."
    "풀어놨던 짐더미에서 세면도구를 꺼냈다.{p}예상에 없던 외박이다. {w}일단은 연락을 해 두는 게 맞겠지."
    $config.rollback_enabled = False
    $message_list.append(Message(type=1, who="", message = "연호야, 자니?"))
    call screen phone_screen 
    $message_list.append(Message(type=0, who="연호", message = "아직 안 잡니다."))
    call screen phone_screen 
    $message_list.append(Message(type=0, who="연호", message = "왜요, 선배?"))
    call screen phone_screen 
    $message_list.append(Message(type=1, who="", message = "상황 어때?"))
    call screen phone_screen 
    $message_list.append(Message(type=0, who="연호", message = "난리 났죠 뭐."))
    call screen phone_screen 
    $message_list.append(Message(type=0, who="연호", message = "오늘은 그냥 안 들어오시는게\n나을 것 같아요."))
    call screen phone_screen 
    $message_list.append(Message(type=1, who="", message = "나 오늘은 아마\n식장에서 자고 갈 것 같아."))
    call screen phone_screen 
    $message_list.append(Message(type=0, who="연호", message = "아... 죄송합니다.\n저도 같이 갔어야 했는데..."))
    call screen phone_screen 
    $message_list.clear()
    $message_list.append(Message(type=1, who="", message = "아냐. 아무리 그래도\n네가 빠져나오면 안되지."))
    call screen phone_screen 
    $message_list.append(Message(type=1, who="", message = "내일 아침에 보자."))
    call screen phone_screen 
    $message_list.append(Message(type=0, who="연호", message = "예.\n뒷문 열어 놓을게요."))
    call screen phone_screen 
    $message_list.append(Message(type=1, who="", message = "고맙다."))
    call screen phone_screen 
    $message_list.append(Message(type=0, who="연호", message = "안녕히주무세요."))
    call screen phone_screen    
    $renpy.block_rollback()
    $config.rollback_enabled = True
    chunyul "나 씻고 올게." 
    ginsetsu "화장실은 나가서 오른쪽으로 가면 바로야."
    chunyul "땡큐."
    window hide
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_funeral with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_toilet with dissolve
    play looping brush
    "언제였던가. {w}한 번.{w} 실수를 가장한 채 녀석이 화장실로 숨어든 적이 있었다."
    "시간은 새벽 3시. {w}소등 이후에도 아침부터 연이어졌던 일들로 인해 쉬이 잠을 이루지 못했던 나는 그 날도 변기에 앉아 이지러지는 전등빛 아래에서 책을 읽고 있었다."
    chunyul "(\"여~ 천율\"?)"
    "아니었다. {w}그보다 엄엄했다."
    chunyul "(\"천율아\"?)"
    "아니었다. {w}그런 다정한 호칭으로 나를 부르는 것은 금기였으니까."
    chunyul "(\"잠깐 나갈까?\")"
    "그랬다. {w}그 한 겨울. {w}바깥 공기는 지내왔던 그 모든 순간을 통틀어서도 유난히 차가웠었다."
    "이미 깊이 골아떨어진 사감. {w}CCTV는 표독스레 붉은 눈을 치켜뜨며 우리를 빤히 응시했지만 창문 틈으로 기숙사 바깥으로 나올 때까지 어떤 이변도 일어나지 않았었다."
    chunyul "(그게 벌써... {w}반 년 가까이 됐나.)"
    "지엄의 고통, 충동의 바다. {w}새로운 것이라곤 하나 남지 않은. {w}태양에게마저 버림받은 황량한 폐허 속에서 과거를 파먹으며 살아가는 자들의 이야기."
    "안정이라는 단어와는 한참 떨어져 있을 폭풍우 치는 바다 위에서도 그 파도에 삼켜지지 않고 살아올 수 있었던 것은 그 애가 내 옆에 있었기 때문이다."
    "새삼. {w}실감하였다. {w}이제 이 하늘 아래에는. {w}나를 진정으로 이해해주고. {w}나와 진심으로 교류해주었던 벗을 잃었다.{p}이제 나는 과거로 돌아가. {w}누구에게도 헤아려지지 못하고. {w}누구도 받아들이지 않는 석상의 모습으로 되돌아갈 것이다."
    "2년여의 시간. {w}나는 사랑받아왔다. {w}분에 넘치도록.{p}그리고 호의에 취해버린 나는 어느덧 그것이 당연하다고 여기고 말았던 것이다."
    "엉덩이까지 내려오는 정돈되지 않아 사방으로 뻗친 머리카락. {w}헐렁한 파란색 생활복. {w}그리고. {w}끝 모르게 깊은 짙은 갈색 눈동자. {w}언제나 쉬어있던 목소리."
    "그 모든 것보다 먼저 생각나는 것은. {w}때때로 그 입술에서. {w}손끝에서. {w}피어나곤 했던 바알간 줄기를 가진 희끄무레한 안개꽃이었다."
    "늘상 내게. {w}억압과 분노. {w}무력의 메타포로 남아있던 종이 타는 냄새와. {w}찰칵, 거리는 부싯소리를.{p}정반대의 의미로 바꾸어낼 만큼. {w}때 놓을 수 없는 물건."
    "이제 남은 것은. {w}무엇일까. {w}불확실한 미래와. {w}의심과 분노만으로 채워진 현재. {w}원망과 후회 투성이의 과거."
    "거울을 바라보았다."
    scene bg_toilet:
        linear 1.0 blur 5.0
    chunyul "...?"
    "시야가 흐려졌다. {w}손등으로 살며시 눈가를 훔쳤다."
    scene bg_toilet with dissolve
    chunyul "...그럼 그렇지."
    "세면대에서 튄 물방울이 눈에 들어간 듯 했다.{p}아직 내게는 그럴 여유도.{w} 자격도 없다. {w}생명과 맞바꾸어 지펴낸 마지막 횃불. {w}그 불길의 정체성과 방향을 정하는 것은 다른 누구도 아닌 내가 될 것이다."
    "우리 모두가 한 때 꿈꿔왔던 것을 이루기 위해. {w}그리고, 곧 다가올 파국으로 치닫는 미래를 막기 위해서라도. {w}나는 달려야만 한다. {w}앞으로 나아가기 위한 잠시간의 휴식이라면 모를까. {w}안거하기 위해 눈과 귀를 닫기에는 시기상조이다."
    chunyul "(조금만 기다려 줘. {w}지켜봐 줘. {w}널 위해서라도. {w}반드시... {w}반드시 바꿔 보일 테니까...)"
    "아직 모든 이들이 굴복한 것은 아니다. {w}아직 모든 이들이 굴종의 대가로 내려진 알량한 떡고물에 눈이 먼 것은 아니다."
    "고개를 들고 돌아가리라. {w}어떤 시선도 감내하리라. {w}감겨진 족쇄를 끊기 위해서. {w}해방을 맞이하기 위해서."
    stop looping
    $SoundPlayer("gargl.ogg", 6.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_funeral with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    chunyul "누나~?"
    "누나는 방 안에 없는 듯 했다."
    chunyul "누나~ {w}없어?"
    play sound walk_slow
    "복도를 따라 건물 밖으로 나가 보았다."
    scene bg_taba 
    show ginsetsu_taba at right
    with dissolve
    chunyul "누나?"
    $Smoking("ginsetsu", loc=2, rep = 1)
    ginsetsu "가까이 오지 마."
    "익숙한 향취가 주변을 떠돌고 있다."
    chunyul "이거... {w}블루벨이지?"
    ginsetsu "뭐?"
    chunyul "블루벨. {w}그 파란생 갑에 종 그려져 있는거."
    ginsetsu "맞긴 한데... {w}어떻게 알았어?"
    chunyul "그냥. {w}한 번 찍어봤어."
    ginsetsu "거짓말."
    $Smoking("ginsetsu", loc=2, rep = 1)
    ginsetsu "나도 알만큼 알고 있어."
    chunyul "......."
    ginsetsu "저리 가라니까. {w}간접흡연이 몸에 제일 나빠."
    chunyul "나도 한 대 받을 수 있을까."
    $Smoking("ginsetsu", loc=2, rep = 1)
    ginsetsu "자."
    show bluebell with dissolve
    $renpy.pause()
    hide bluebell with Dissolve(1.0)
    ginsetsu "어떻게 하는지는 알아?"
    chunyul "...아마도."
    "꺼내 물었다."
    $SoundPlayer("lighter.ogg", 3.0)
    $SoundPlayer("lighter.ogg", 3.0)
    $SoundPlayer("lighter.ogg", 3.0)
    chunyul "......."
    $Smoking("ginsetsu", loc=2, rep = 1)
    ginsetsu "빨아들이면서 붙여야지."
    $SoundPlayer("lighter.ogg", 6.0)
    play second cough
    $SoundPlayer("smoke.ogg", 2.0)
    $renpy.pause()
    return