# coding: utf-8
import cv2
# import string

def main():

    while True :
        file_name = input("ファイル名を入力してください\n")                                     
        new_file_name = "./" + input("新しいファイル名を入力してください\n")                                        
        video = cv2.VideoCapture(file_name)                                                     # videoオブジェクト作成
        if video.isOpened() == True :                                                           # ファイルの確認
            new_video_len_sec = input("ファイルの長さを指定してください(秒)\n")                 # 新しい動画の長さを読み込む
            new_video_len_sec = int(new_video_len_sec) -1                                       # 新しい動画の秒数を指定
            width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))                                    # フレームの幅を取得
            height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))                                  # フレームの高さを取得
            size = (width, height)                                                              # フレームのサイズを格納
            video_frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)                             # フレーム数を取得
            video_fps = video.get(cv2.CAP_PROP_FPS)                                             # フレームレートを取得
            video_len_sec = int(video_frame_count / video_fps)                                  # 長さ（秒）を取得
            shortening_video_len_sec = new_video_len_sec                                        # 新しい動画の長さ（秒）を入力        
            ratio = shortening_video_len_sec / video_len_sec                                    # 短縮したい比率を取得
            shortening_video_fps = int(video_fps/ratio)                                         # 短縮したフレームレートを取得
            shortening_video_frame = int(video_frame_count/ratio)                               # 短縮したフレーム数を取得
            fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                                    # ファイル形式を指定(mp4)
            writer = cv2.VideoWriter(new_file_name, fmt, shortening_video_fps, size)            # ライター作成（第１引数：保存ファイルパス、第２引数：ファイル形式、第３引数：フレームレート、第４引数：画面サイズ）
            print("ファイルを書き出し中・・・")
            for i in range(shortening_video_frame):                                             # フレームから動画作成
                ret, frame = video.read()
                writer.write(frame)               
            writer.release()
            video.release()
            cv2.destroyAllWindows()
            print("完了")
            break
        else :
            print("ファイル名が間違っているか存在しません")
            continue

if __name__ == "__main__":
    main()