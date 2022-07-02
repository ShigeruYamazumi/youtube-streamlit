import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!!'

#st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('ここは右カラム')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander1 = st.expander('問い合わせ2')
expander1.write('問い合わせ回答2')
expander1 = st.expander('問い合わせ3')
expander1.write('問い合わせ回答3')

#'あなたの趣味：', text
#'コンデション', condition

#
# テキスト入力
#
#st.sidebar.write('Interactive Widgets')

#text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

#'あなたの趣味：', text
#'コンデション', condition


#
# セレクトボックス
#
#st.write('Display Image')
#option = st.selectbox(
#    'あなたの好きな数字を教えて下さい。',
#    list(range(1, 11))
#) 
#'あなたの好きな数字は、', option, 'です。'
 
#
# チェックボックス写真表示
#
#st.write('Display Image')
#if st.checkbox('Show Imge'):
#    img = Image.open('/home/shigeru/picture/男厨会/2016男厨会クリスマス/写真 2016-12-18 15 57 20.jpg')
#    st.image(img, caption='クリスマス', use_column_width=True)

#
# マップ表示
#
#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)

#st.map(df)

#
# グラフ表示
#st.write('DataFrame')

#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)
#st.bar_chart(df)
#st.line_chart(df)

