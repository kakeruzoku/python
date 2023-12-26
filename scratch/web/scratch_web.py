ver = "α1.1"
kousin_rireki = """更新履歴

α1.1 exe版公開
α1.0 公開"""

print("バージョン:",ver)
#インポート
try:
    import sys
    import PySimpleGUI as sg
    import scratchattach as s3
    import traceback
except:
    print("正しく読み込めませんでした。")
    #print("次のプログラムをpipでインストールしてください。")
    #print("・PySimpleGUI")
    #print("・scratchattach")
    sys.exit()

try:
    #初期設定
    sg.theme("DarkTeal2")
    mode = "login"#画面を表す
    
    #helpテキストの事前用意
    help_login = """Qログイン出来ません。
A次の可能性があります。
・パスワードまたはユーザー名またはログインセッションが違う
・ログイン方法の選択が違う
・IPBANまたはBANされている

ログインセッションの探し方
・scratch.mit.eduのcookieを探します。
・「scratchsessionid」を選択します。
・コンテンツを全てコピーします。
※現在セッションログインの入力を間違えても続行ができてしまうため、パスワードログインをお勧めします。"""
    welcome = """ようこそ!
※始める前に必ずIDLEを確認し、警告(青字)が出ていないか確認してください。エラーが出ていた場合は「何か文章が出てきた場合」を見てください。また、scratchサーバーの負荷をかけるようなことはおやめください。
TimMcCool作scratchattachとPySimpleGUIを使用しています。
https://x.gd/kakeru_scpy を必ず確認してください。
"""
    help_login_session = """Warning: The account you logged in to is BANNED. Some features may not work properly.
    訳:垢BANされています。\nWarning: Logged in, but couldn't fetch XToken.
    Some features (including cloud variables) will not work properly. To get cloud variables to work, provide a username argument: Session('session_id', username='username')
    If you're using an online IDE (like replit.com) Scratch possibly banned its IP adress.　または　
    Warning: Logged in, but couldn't fetch XToken. Cloud variables will still work, but other features may not work properly.
    If you're using an online IDE (like replit.com) Scratch possibly banned its IP adress.
    訳:XTokenが取得できなかったため、ログインされていますが、一部の機能は使えません。
    Your network is blocked or rate-limited by Scratch.\nIf you're using an online IDE like replit.com, try running the code on your computer.
    訳:IPBANされています。別のIPを利用してください。

    これらが表示された場合は、再ログインしてください。これを続行したことに対する不具合の報告は受け付けません。"""
    
    deta_syutoku = True
    
    def layout(gamen):#画面用意
        global deta_syutoku
        global key_ID
        if gamen == "login":#ログイン画面
            def_layout = [[sg.T("welcome to scratch in python!"),sg.B("更新履歴" , k="kousin_rireki")],
                            [sg.T("--------------------")],
                            [sg.T("ログインをしない場合はこちら")],
                            [sg.B("ログインしない" , k="login_no")],
                            [sg.T("--------------------")],
                            [sg.T("ログインする")],
                            [sg.Radio("パスワードログイン" , group_id="login_mode" , k="login_m_pass" , default=True) , sg.Radio("セッションログイン" , group_id="login_mode" , k="login_m_session")],
                            [sg.I("ユーザー名" , k="login_user")],
                            [sg.I("パスワード" , k="login_pass")],
                            [sg.I("セッションID" , k="login_session")],
                            [sg.B("ログイン" , k="login_login"),sg.B("ヘルプ" , k="login_help")],
                            [sg.T("" , k="login_sita")]]
            def_ookisa = 400,350
            def_name = "scratchWEB/login"
        elif gamen == "welcome":#ようこそ
            def_layout = [[sg.T("情報"),sg.Checkbox("確認しました。", default=False, k="welcome_OK"),sg.B("ログインし直す" , k="welcome_back")],
                          [sg.ML(welcome , size=(50,16))],
                          [sg.B("確認した上でトップページへ" , k="welcome_go_home"),sg.B("何か文章が出てきた場合" ,  k="login_session_help")]]
            def_ookisa = 400,350
            def_name = "ようこそ！"
        elif gamen == "home":#ホーム画面
            deta_syutoku = True
            def_layout = [home_login_text(1),
                          [sg.T("")],
                          [sg.T("トップデータ"),sg.B("scratchニュース",k="home_news"),sg.B("注目のプロジェクト",k="home_FP"),sg.B("注目のスタジオ",k="home_FS"),sg.B("統計情報",k="home_toukei")],
                          [sg.B("コミュニティの好きなもの",k="home_love"),sg.B("コミュニティのリミックス",k="home_remix")],
                          home_login_text(2),
                          [sg.T("")],
                          [sg.T("検索"),sg.I("検索内容",size=50),sg.B("検索")],
                          [sg.Radio("プロジェクト",group_id="search",default=True),sg.Radio("スタジオ",group_id="search"),sg.Radio("フォーラムの投稿",group_id="search")],
                          [sg.T("")],
                          [sg.T("IDを入力してアクセス")],
                          [sg.T("プロジェクト",size=25),sg.I("IDを入力",size=50),sg.B("アクセス！")],
                          [sg.T("スタジオ",size=25),sg.I("IDを入力",size=50),sg.B("アクセス！")],
                          [sg.T("ユーザー",size=25),sg.I("IDを入力",size=50),sg.B("アクセス！")],
                          [sg.T("フォーラムのトピック",size=25),sg.I("IDを入力",size=50),sg.B("アクセス！")],
                          [sg.T("フォーラムの投稿",size=25),sg.I("IDを入力",size=50),sg.B("アクセス！")],
                          [sg.T("URL",size=25),sg.I("https://scratch.mit.edu/",size=50),sg.B("アクセス！")]]
            def_ookisa = 700,500
            def_name = "Scratch - 想像、プログラム、共有"
        elif gamen == "home_news":
            deta_syutoku = False
            def_layout = [[sg.B("scratch",k="go_home"),sg.T("Scratchnews!")],
                          [sg.B(home_news(0),size=50,k="key_0"),sg.T("最新")],
                          [sg.B(home_news(1),size=50,k="key_1")],
                          [sg.B(home_news(2),size=50,k="key_2")],
                          [sg.B(home_news(3),size=50,k="key_3")],
                          [sg.B(home_news(4),size=50,k="key_4")],
                          [sg.B(home_news(5),size=50,k="key_5")],
                          [sg.B(home_news(6),size=50,k="key_6")],
                          [sg.B(home_news(7),size=50,k="key_7")],
                              [sg.B(home_news(8),size=50,k="key_8")],
                          [sg.B(home_news(9),size=50,k="key_9")]]
            def_ookisa = 500,400
            def_name = "scratchnews"
        elif gamen == "home_news_S":
            deta_syutoku = False
            global home_news_D
            def_layout = [[sg.B("scratch",k="go_home"),sg.B("Scratchnews TOP",k="home_news")],
                          [sg.T("")],
                          [sg.T(f"タイトル:{home_news_D[key_ID]['headline']}")],
                          [sg.B("サイトへ行く！")],
                          [sg.T("")],
                          [sg.ML(f"{home_news_D[key_ID]['copy']}",size=(50,8))]]
            def_ookisa = 400,300
            def_name = home_news_D[key_ID]['headline']
        elif gamen == "home_FP":
            deta_syutoku = False
            def_layout = [[sg.B("scratch",k="go_home"),sg.T("注目のプロジェクト")],
                          [sg.B(home_FP(0),size=50,k="key_0"),sg.T("最新")],
                          [sg.B(home_FP(1),size=50,k="key_1")],
                          [sg.B(home_FP(2),size=50,k="key_2")],
                          [sg.B(home_FP(3),size=50,k="key_3")],
                          [sg.B(home_FP(4),size=50,k="key_4")],
                          [sg.B(home_FP(5),size=50,k="key_5")],
                          [sg.B(home_FP(6),size=50,k="key_6")],
                          [sg.B(home_FP(7),size=50,k="key_7")],
                          [sg.B(home_FP(8),size=50,k="key_8")],
                          [sg.B(home_FP(9),size=50,k="key_9")],
                          [sg.B(home_FP(10),size=50,k="key_10")],
                          [sg.B(home_FP(11),size=50,k="key_11")],
                          [sg.B(home_FP(12),size=50,k="key_12")],
                          [sg.B(home_FP(13),size=50,k="key_13")],
                          [sg.B(home_FP(14),size=50,k="key_14")],
                          [sg.B(home_FP(15),size=50,k="key_15")],
                          [sg.B(home_FP(16),size=50,k="key_16")],
                          [sg.B(home_FP(17),size=50,k="key_17")],
                          [sg.B(home_FP(18),size=50,k="key_18")],
                          [sg.B(home_FP(19),size=50,k="key_19")]]
            def_ookisa = 500,700
            def_name = "注目のプロジェクト"
        elif gamen == "home_FP_S":
            deta_syutoku = False
            global home_FP_D
            def_layout = [[sg.B("scratch",k="go_home"),sg.B("注目のプロジェクト TOP",k="home_FP")],
                          [sg.T("")],
                          [sg.T(f"{home_FP_D[key_ID]['title']}")],
                          [sg.T(f"作:@{home_FP_D[key_ID]['creator']},{home_FP_D[key_ID]['love_count']}ハート")],
                          [sg.B("プロジェクトへ行く！")]]
            def_ookisa = 400,200
            def_name = home_FP_D[key_ID]['title']
        elif gamen == "home_FS":
            deta_syutoku = False
            def_layout = [[sg.B("scratch",k="go_home"),sg.T("注目のスタジオ")],
                          [sg.B(home_FS(0),size=50,k="key_0"),sg.T("最新")],
                          [sg.B(home_FS(1),size=50,k="key_1")],
                          [sg.B(home_FS(2),size=50,k="key_2")],
                          [sg.B(home_FS(3),size=50,k="key_3")],
                          [sg.B(home_FS(4),size=50,k="key_4")]]
            def_ookisa = 500,350
            def_name = "注目のスタジオ"
        elif gamen == "home_FS_S":
            deta_syutoku = False
            global home_FS_D
            def_layout = [[sg.B("scratch",k="go_home"),sg.B("注目のスタジオ TOP",k="home_FS")],
                          [sg.T("")],
                          [sg.T(f"{home_FS_D[key_ID]['title']}")],
                          [sg.B("スタジオへ行く！")]]
            def_ookisa = 400,200
            def_name = home_FS_D[key_ID]['title']
        elif gamen == "home_love":
            deta_syutoku = False
            def_layout = [[sg.B("scratch",k="go_home"),sg.T("コミュニティの好きなもの")],
                          [sg.B(home_love(0),size=50,k="key_0"),sg.T("最新")],
                          [sg.B(home_love(1),size=50,k="key_1")],
                          [sg.B(home_love(2),size=50,k="key_2")],
                          [sg.B(home_love(3),size=50,k="key_3")],
                          [sg.B(home_love(4),size=50,k="key_4")],
                          [sg.B(home_love(5),size=50,k="key_5")],
                          [sg.B(home_love(6),size=50,k="key_6")],
                          [sg.B(home_love(7),size=50,k="key_7")],
                          [sg.B(home_love(8),size=50,k="key_8")],
                          [sg.B(home_love(9),size=50,k="key_9")],
                          [sg.B(home_love(10),size=50,k="key_10")],
                          [sg.B(home_love(11),size=50,k="key_11")],
                          [sg.B(home_love(12),size=50,k="key_12")],
                          [sg.B(home_love(13),size=50,k="key_13")],
                          [sg.B(home_love(14),size=50,k="key_14")],
                          [sg.B(home_love(15),size=50,k="key_15")],
                          [sg.B(home_love(16),size=50,k="key_16")],
                          [sg.B(home_love(17),size=50,k="key_17")],
                          [sg.B(home_love(18),size=50,k="key_18")],
                          [sg.B(home_love(19),size=50,k="key_19")]]
            def_ookisa = 500,700
            def_name = "コミュニティの好きなもの"
        elif gamen == "home_love_S":
            deta_syutoku = False
            global home_love_D
            def_layout = [[sg.B("scratch",k="go_home"),sg.B("コミュニティの好きなもの TOP",k="home_love")],
                          [sg.T("")],
                          [sg.T(f"{home_love_D[key_ID]['title']}")],
                          [sg.T(f"作:@{home_love_D[key_ID]['creator']},{home_love_D[key_ID]['love_count']}ハート")],
                          [sg.B("プロジェクトへ行く！")]]
            def_ookisa = 400,200
            def_name = home_love_D[key_ID]['title']
        elif gamen == "home_remix":
            deta_syutoku = False
            def_layout = [[sg.B("scratch",k="go_home"),sg.T("コミュニティでリミックスされているもの")],
                          [sg.B(home_remix(0),size=50,k="key_0"),sg.T("最新")],
                          [sg.B(home_remix(1),size=50,k="key_1")],
                          [sg.B(home_remix(2),size=50,k="key_2")],
                          [sg.B(home_remix(3),size=50,k="key_3")],
                          [sg.B(home_remix(4),size=50,k="key_4")],
                          [sg.B(home_remix(5),size=50,k="key_5")],
                          [sg.B(home_remix(6),size=50,k="key_6")],
                          [sg.B(home_remix(7),size=50,k="key_7")],
                          [sg.B(home_remix(8),size=50,k="key_8")],
                          [sg.B(home_remix(9),size=50,k="key_9")],
                          [sg.B(home_remix(10),size=50,k="key_10")],
                          [sg.B(home_remix(11),size=50,k="key_11")],
                          [sg.B(home_remix(12),size=50,k="key_12")],
                          [sg.B(home_remix(13),size=50,k="key_13")],
                          [sg.B(home_remix(14),size=50,k="key_14")],
                          [sg.B(home_remix(15),size=50,k="key_15")],
                          [sg.B(home_remix(16),size=50,k="key_16")],
                          [sg.B(home_remix(17),size=50,k="key_17")],
                          [sg.B(home_remix(18),size=50,k="key_18")],
                          [sg.B(home_remix(19),size=50,k="key_19")]]
            def_ookisa = 500,700
            def_name = "コミュニティでリミックスされているもの"
        elif gamen == "home_remix_S":
            deta_syutoku = False
            global home_remix_D
            def_layout = [[sg.B("scratch",k="go_home"),sg.B("コミュニティでリミックスされているもの TOP",k="home_remix")],
                          [sg.T("")],
                          [sg.T(f"{home_remix_D[key_ID]['title']}")],
                          [sg.T(f"作:@{home_remix_D[key_ID]['creator']},{home_remix_D[key_ID]['remixers_count']}リミックス")],
                          [sg.B("プロジェクトへ行く！")]]
            def_ookisa = 400,200
            def_name = home_remix_D[key_ID]['title']
        elif gamen == "home_toukei":
            deta_syutoku = False
            def_layout = [[sg.B("scratch",k="go_home"),sg.T("統計情報")],
                          [sg.T(f"ユーザー数:{home_toukei_D['USER_COUNT']}/プロフィールコメント数:{home_toukei_D['PROFILE_COMMENT_COUNT']}")],
                          [sg.T(f"プロジェクト数:{home_toukei_D['PROJECT_COUNT']}プロジェクトコメント数:{home_toukei_D['PROJECT_COMMENT_COUNT']}")],
                          [sg.T(f"スタジオ数:{home_toukei_D['STUDIO_COUNT']}/スタジオコメント数:{home_toukei_D['STUDIO_COMMENT_COUNT']}")],
                          [sg.T(f"総コメント数:{home_toukei_D['COMMENT_COUNT']}")]]
            def_ookisa = 500,200
            def_name = "統計情報"
        elif gamen == "my_account":
            def_layout = [[sg.B("scratch",k="go_home"),sg.T("アカウントメニュー")],
                          [sg.B("ログアウトする",k="welcome_back")]]
            def_ookisa = 300,100
            def_name = "アカウントメニュー"
        return [def_layout,def_ookisa,def_name]

    def hyouzi(deta):#画面描画
        return sg.Window(deta[2], deta[0] , finalize=True , size=(deta[1]))
    
    def home_login_text(bangou):
        global window
        global login_session
        if bangou == 1:
            if if_login:
                return [sg.B("scratch"),sg.B("傾向"),sg.B("ディスカッションフォーラム"),sg.B("メッセージ"+str(login_session.message_count())+"件"),sg.B(login_session.get_linked_user(),k="my_account")]
            else:
                return [sg.B("scratch"),sg.B("傾向"),sg.B("ディスカッションフォーラム"),sg.B("ログインする",k="my_account")]
        elif bangou == 2:
            if if_login:
                return [sg.T("ログイン者のみ"),sg.B("フォロー中の人の更新",k="home_follow"),sg.B("フォロー中の人の好きなもの",k="home_follow_love")]
            else:
                return [sg.T("ログイン者のみ フォロー中の人の更新 フォロー中の人の好きなもの")]
    
    def key_load(atai):
        global key_ID
        key_ID = atai
        global mode
        global window
        if mode == "home_news":
            mode = "home_news_S"
            window.close()
            window = hyouzi(layout("home_news_S"))
        elif mode == "home_FP":
            mode = "home_FP_S"
            window.close()
            window = hyouzi(layout("home_FP_S"))
        elif mode == "home_FS":
            mode = "home_FS_S"
            window.close()
            window = hyouzi(layout("home_FS_S"))
        elif mode == "home_love":
            mode = "home_love_S"
            window.close()
            window = hyouzi(layout("home_love_S"))
        elif mode == "home_remix":
            mode = "home_remix_S"
            window.close()
            window = hyouzi(layout("home_remix_S"))
    
    def help_pege(naiyou):
        if naiyou == "login":
            def_help = [[sg.T("help/ログイン")],
                        [sg.ML(help_login , size=(50,20))]]
            def_help_ookisa = 400,400
        if naiyou == "login_session":
            def_help = [[sg.T("help/ログインエラー")],
                        [sg.ML(help_login_session , size=(110,15))]]
            def_help_ookisa = 800,300
        if naiyou == "kousin_rireki":
            global kousin_rireki
            def_help = [[sg.T("help/更新履歴 ver:"),sg.T(ver)],
                        [sg.ML(kousin_rireki , size=(50,20))]]
            def_help_ookisa = 400,400
        return sg.Window("ヘルプページ", def_help , finalize=True , size=(def_help_ookisa))
    
    def home_news(atai):
        global home_news_D
        if len(home_news_D[atai]['headline']) > 40:
            home_memo = f"{home_news_D[atai]['headline'][:39]}..."
        else:
            home_memo = home_news_D[atai]['headline']
        return home_memo
    
    def home_FP(atai):
        global home_FP_D
        if len(home_FP_D[atai]['title']) > 20:
            home_memo = f"{home_FP_D[atai]['title'][:19]}... 作:@{home_FP_D[atai]['creator']}"
        else:
            home_memo = f"{home_FP_D[atai]['title']} 作:@{home_FP_D[atai]['creator']}"
        return home_memo
    
    def home_FS(atai):
        global home_FS_D
        if len(home_FS_D[atai]['title']) > 40:
            home_memo = f"{home_FS_D[atai]['title'][:39]}..."
        else:
            home_memo = f"{home_FS_D[atai]['title']}"
        return home_memo
    
    def home_love(atai):
        global home_love_D#f"タイトル:{home_D[atai]['title']} 作者{home_D[atai]['creator']} ハート{home_D[atai]['love_count']}\nプロジェクトURL:https://scratch.mit.edu/projects/{home_D[atai]['id']} ID:{home_D[atai]['id']}"
        if len(home_love_D[atai]['title']) > 20:
            home_memo = f"{home_love_D[atai]['title'][:19]}... 作:@{home_love_D[atai]['creator']},{home_love_D[atai]['love_count']}ハート"
        else:
            home_memo = f"{home_love_D[atai]['title']} 作:@{home_love_D[atai]['creator']},{home_love_D[atai]['love_count']}ハート"
        return home_memo
    
    def home_remix(atai):
        global home_remix_D#f"タイトル:{home_D[atai]['title']} 作者{home_D[atai]['creator']} ハート{home_D[atai]['love_count']}\nプロジェクトURL:https://scratch.mit.edu/projects/{home_D[atai]['id']} ID:{home_D[atai]['id']}"
        if len(home_remix_D[atai]['title']) > 20:
            home_memo = f"{home_remix_D[atai]['title'][:19]}... 作:@{home_remix_D[atai]['creator']},{home_remix_D[atai]['remixers_count']}リミックス"
        else:
            home_memo = f"{home_remix_D[atai]['title']} 作:@{home_remix_D[atai]['creator']},{home_remix_D[atai]['remixers_count']}リミックス"
        return home_memo
    
    window = hyouzi(layout("login"))
    print("正常に起動しました。")
    
    while True:
        e, v = window.read()
    
        if e == sg.WIN_CLOSED or e == "Exit":
            break

        elif e == "kousin_rireki":
            help_window = help_pege("kousin_rireki")

        elif e == "login_no":#未ログイン
            mode = "welcome"
            if_login = False
            window.close()
            window = hyouzi(layout("welcome"))
    
        elif e == "login_login":#ログインする
            if_login = True
            try:
                if v["login_m_pass"] == True:
                    login_session = s3.login(v["login_user"], v["login_pass"])
                else:
                    login_session = s3.Session(v["login_session"], username=v["login_user"])
            except Exception as e:
                window["login_sita"].update("ログインに失敗しました。もう一度お試しください。")
            else:
                try:
                    if login_session.banned:
                        window["login_sita"].update("ログインしたアカウントはBANされています")
                    else:
                        mode = "welcome"
                        window.close()
                        window = hyouzi(layout("welcome"))
                except Exception as e:
                    window["login_sita"].update("ログインに失敗しました。もう一度お試しください。")
        

        elif e == "login_help":#ログインヘルプ
            help_window = help_pege("login")

        elif e == "welcome_go_home":
            if v["welcome_OK"]:
                mode = "home"
                window.close()
                window = hyouzi(layout("home"))

        elif e == "go_home":#トップ
            mode = "home"
            window.close()
            window = hyouzi(layout("home"))

        elif e == "login_session_help":#警告について
            help_window = help_pege("login_session")

        elif e == "welcome_back":#再ログイン
            mode = "login"
            window.close()
            window = hyouzi(layout("login"))

        elif e == "home_news":#scratchニュース
            mode = "home_news"
            if deta_syutoku:
                home_news_D = s3.get_news(limit=10, offset=0)
            window.close()
            window = hyouzi(layout("home_news"))

        elif e == "home_FP":#注目のプロジェクト
            mode = "home_FP"
            if deta_syutoku:
                home_FP_D = s3.featured_projects()
            window.close()
            window = hyouzi(layout("home_FP"))

        elif e == "home_FS":#注目のスタジオ
            mode = "home_FS"
            if deta_syutoku:
                home_FS_D = s3.featured_studios()
            window.close()
            window = hyouzi(layout("home_FS"))

        elif e == "my_account":
            if if_login:
                mode = "my_account"
                window.close()
                window = hyouzi(layout("my_account"))
            else:
                mode = "login"
                window.close()
                window = hyouzi(layout("login"))

        elif e == "home_love":#ハート
            mode = "home_love"
            if deta_syutoku:
                home_love_D = s3.top_loved()
            window.close()
            window = hyouzi(layout("home_love"))

        elif e == "home_remix":#リミックス
            mode = "home_remix"
            if deta_syutoku:
                home_remix_D = s3.top_remixed()
            window.close()
            window = hyouzi(layout("home_remix"))

        elif e == "home_toukei":#統計情報
            mode = "home_toukei"
            if deta_syutoku:
                home_toukei_D = s3.total_site_stats()
            window.close()
            window = hyouzi(layout("home_toukei"))

        elif e == "key_0":
            key_load(0)

        elif e == "key_1":
            key_load(1)

        elif e == "key_2":
            key_load(2)

        elif e == "key_3":
            key_load(3)

        elif e == "key_4":
            key_load(4)

        elif e == "key_5":
            key_load(5)

        elif e == "key_6":
            key_load(6)

        elif e == "key_7":
            key_load(7)

        elif e == "key_8":
            key_load(8)

        elif e == "key_9":
            key_load(9)

        elif e == "key_10":
            key_load(10)

        elif e == "key_11":
            key_load(11)

        elif e == "key_12":
            key_load(12)

        elif e == "key_13":
            key_load(13)

        elif e == "key_14":
            key_load(14)

        elif e == "key_15":
            key_load(15)

        elif e == "key_16":
            key_load(16)

        elif e == "key_17":
            key_load(17)

        elif e == "key_18":
            key_load(18)

        elif e == "key_19":
            key_load(19)
except:
    print("エラーが発生しました。")
    window.close()
    print(":エラー:")
    traceback.print_exc()
    print("終了しました。")
else:
    print("正常に終了しました。")
    window.close()
