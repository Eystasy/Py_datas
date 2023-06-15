def dwm(info_list):
    # 下载歌曲
    index = 1
    while index ==1:
        index = int(input('请输入你要下载的歌曲序号（按Ctrl+C可退出,按1000可下载整页歌曲):'))
        if index == 1000:
            for info in info_list:
                info_url = info[2]
                music_url = requests.get(info_url).json()['data']['url']
                music_data = requests.get(music_url).content
                print(f'music{info[0]}-{info[1]}下载成功！')
                # open(f'music/{info[0]}-{info[1]}.mp3', mode='wb').write(music_data)
                open(f'{info[0]}-{info[1]}.mp3', mode='wb').write(music_data)
        else:
            info = info_list[index]
            info_url = info[2]
            music_url = requests.get(info_url).json()['data']['url']
            music_data = requests.get(music_url).content
            print(f'music{info[0]}-{info[1]}下载成功！')
            # open(f'music/{info[0]}-{info[1]}.mp3', mode='wb').write(music_data)
            open(f'{info[0]}-{info[1]}.mp3', mode='wb').write(music_data)
