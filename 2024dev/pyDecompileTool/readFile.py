import re

def readFile(filePath):
    content=""
    try:
        with open(filePath, 'r', encoding='utf-16') as file:
            lines = file.readlines()
            caller_class = ""
            caller_class_method=""
            for line in lines:
                #classを特定
                a=call_class(line.strip())
                if a and a!=caller_class:
                    print('class '+a)
                    # content = content + line.strip()
                    caller_class=a
                #callメソッドを特定
                b=call_matcher(line.strip())
                if b and b.strip()!=caller_class:
                    caller_class_method=caller_class+'.'+b+ '->'
                    print('method '+caller_class_method)
                    # content = content + line.strip()
                #calleeクラスメソッドを特定
                c=callee_matcher(line.strip(),caller_class)
                if c:
                    print('★'+caller_class_method+c)
                    content = content + caller_class_method+c+'\n'
    except FileNotFoundError as e:
            print(f"ファイルが見つかりません。:{e}")
    except Exception as e:
            print(f"ファイル読み込み中にエラーが発生しました。:{e}")
    finally:
        file.close()
    return content
def call_class(dat):
    pattern0=r'public class'
    if re.search(pattern0,dat):
        p_start= dat.find('.')
        p_last=dat.find('{')
        edit_dat=dat[p_start+1:p_last-1] 
        return edit_dat
def call_matcher(dat):
    # 正規表現パターン 
    pattern1 = r'^public|private.*\(\);$'
    if re.match(pattern1, dat):
        # p_start= dat.find('(')
        p_last=dat.find('(')
        edit_dat=dat[:p_last] 
        print('----'+edit_dat)
        # edit_dat=edit_dat.replace('{','')
        revName=""
        for char in reversed(edit_dat):
            if char == " ":
                break
            revName=revName + char
        return revName[::-1]
def callee_matcher(dat,prClass):
    # 正規表現パターン 
    pattern2 = r'^(?!.*<init>).*// Method'
    if re.search(pattern2, dat):
        p_start= dat.find('Method')
        p_last=dat.find(':()')
        edit_dat=dat[p_start+7:p_last]
        print('++++' + edit_dat)
        if judge_public_callee(edit_dat)==True:
            revName=""
            for char in reversed(edit_dat):
                if char == "/":
                    break
                revName=revName + char
            return revName[::-1]
        else:
            return prClass+'.'+edit_dat
def judge_public_callee(dat):
    # 正規表現パターン 
    pattern3 = r'.*\..*'
    if re.search(pattern3, dat):
        return True
