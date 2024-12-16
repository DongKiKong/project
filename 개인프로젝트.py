import pyogrio
pyogrio.list_drivers()
import streamlit as st
import openpyxl
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import folium_static

st.title('C011023김동규 - 개인프로젝트')

st.header('윤석열 대통령 비상 계엄 선포 이후, 각종 지표의 변화, 과거 박근혜 탄핵 당시 지표와 비교해보기')

#geojson 파일 처리
gdf_korea_sido = gpd.read_file("./법정구역_시도_simplified.geojson")
gdf_korea_sido.rename(columns={'CTP_KOR_NM':'시도별'},
                      inplace = True)  #컬럼명 변경
#시,도 이름 두글자로 통일해주기
gdf_korea_sido.시도별[0] = '서울'
gdf_korea_sido.시도별[1] = '부산'
gdf_korea_sido.시도별[2] = '대구'
gdf_korea_sido.시도별[3] = '인천'
gdf_korea_sido.시도별[4] = '광주'
gdf_korea_sido.시도별[5] = '대전'
gdf_korea_sido.시도별[6] = '울산'
gdf_korea_sido.시도별[7] = '세종'
gdf_korea_sido.시도별[8] = '경기'
gdf_korea_sido.시도별[9] = '충북'
gdf_korea_sido.시도별[10] = '충남'
gdf_korea_sido.시도별[11] = '전북'
gdf_korea_sido.시도별[12] = '전남'
gdf_korea_sido.시도별[13] = '경북'
gdf_korea_sido.시도별[14] = '경남'
gdf_korea_sido.시도별[15] = '제주'
gdf_korea_sido.시도별[16] = '강원'

#엑셀 파일 처리
df_homeprice = pd.read_excel("./지역별_아파트_평당가격.xlsx",
                             engine='openpyxl',
                             header=2)
df_homeprice.drop([0,1,2,4,5,6,7,8,25,26],axis=0,inplace=True) #쓸 데 없는 행 지우기
#2022대선 당시 지지율 열 추가
df_homeprice['2022대선 당시 지지율'] =[6,12,24,-12,-24,6,9,-9,-12,12,6,6,-24,-24,24,12,-12]
df_homeprice['2022대선 당시 지지율'] = -df_homeprice['2022대선 당시 지지율']
#계엄 이후 민주당 지지율 증감율 열 추가
df_homeprice['계엄 이후 민주당 지지율 증감'] =[4,-5,-10,5,10,8,-5,8,5,5,8,8,10,10,-10,-5,0]
#최순실 사건 전후, 집값 변화 관련 데이터 추가
df_homeprice['최순실 사건 전후, 가격 차이(만원)'] = df_homeprice['2016년 12월'] - df_homeprice['2016년 9월']
df_homeprice['사건 전후, 가격 차이(%)'] = df_homeprice['최순실 사건 전후, 가격 차이(만원)']/df_homeprice['2016년 9월']
    

if st.button('geojson 파일 전처리 과정 보기'):
    st.write('+ 원본 데이터')
    gdf_korea_sido = gpd.read_file("./법정구역_시도_simplified.geojson")
    st.dataframe(gdf_korea_sido)

    gdf_korea_sido.rename(columns={'CTP_KOR_NM':'시도별'},
                      inplace = True)  #컬럼명 변경
    #시,도 이름 두글자로 통일해주기
    gdf_korea_sido.시도별[0] = '서울'
    gdf_korea_sido.시도별[1] = '부산'
    gdf_korea_sido.시도별[2] = '대구'
    gdf_korea_sido.시도별[3] = '인천'
    gdf_korea_sido.시도별[4] = '광주'
    gdf_korea_sido.시도별[5] = '대전'
    gdf_korea_sido.시도별[6] = '울산'
    gdf_korea_sido.시도별[7] = '세종'
    gdf_korea_sido.시도별[8] = '경기'
    gdf_korea_sido.시도별[9] = '충북'
    gdf_korea_sido.시도별[10] = '충남'
    gdf_korea_sido.시도별[11] = '전북'
    gdf_korea_sido.시도별[12] = '전남'
    gdf_korea_sido.시도별[13] = '경북'
    gdf_korea_sido.시도별[14] = '경남'
    gdf_korea_sido.시도별[15] = '제주'
    gdf_korea_sido.시도별[16] = '강원'

    st.write('+ 컬럼명 및 시도이름 변경 후, 데이터')

    st.dataframe(gdf_korea_sido)



if st.button('엑셀 파일 전처리 과정 보기'):
    st.write('+ 원본 데이터')
    df_homeprice = pd.read_excel("./지역별_아파트_평당가격.xlsx",
                             engine='openpyxl',
                             header=2)
    st.dataframe(df_homeprice)

    df_homeprice.drop([0,1,2,4,5,6,7,8,25,26],axis=0,inplace=True) #쓸 데 없는 행 지우기
    #2022대선 당시 지지율 열 추가
    df_homeprice['2022대선 당시 지지율'] =[6,12,24,-12,-24,6,9,-9,-12,12,6,6,-24,-24,24,12,-12]
    df_homeprice['2022대선 당시 지지율'] = -df_homeprice['2022대선 당시 지지율']
    #계엄 이후 민주당 지지율 증감율 열 추가
    df_homeprice['계엄 이후 민주당 지지율 증감'] =[4,-5,-10,5,10,8,-5,8,5,5,8,8,10,10,-10,-5,0]
    #최순실 사건 전후, 집값 변화 관련 데이터 추가
    df_homeprice['최순실 사건 전후, 가격 차이(만원)'] = df_homeprice['2016년 12월'] - df_homeprice['2016년 9월']
    df_homeprice['사건 전후, 가격 차이(%)'] = df_homeprice['최순실 사건 전후, 가격 차이(만원)']/df_homeprice['2016년 9월']
    
    st.write('+ 전처리 및 지지율 관련 열 추가 후, 데이터셋')
    st.dataframe(df_homeprice)

st.write('### 2022대선 당시 국민의힘(윤석열) 우세 지지도')

gu_map_sido = folium.Map(location = [37.541, 126.986], #서울 중심부 시작
                         zoom_start = 7,
                         tiles='cartodbpositron')

folium.Choropleth(
    geo_data = gdf_korea_sido,
    data = df_homeprice,
    columns = ('분류.1','2022대선 당시 지지율'),
    key_on = 'feature.properties.시도별',
    fill_color = 'RdBu',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '국민의힘(윤석열) 우세 지지율'
).add_to(gu_map_sido)

folium_static(gu_map_sido)

if st.button('해석 및 분석 보기1'):
    st.write('+ 해석')
    st.write('대선 당시: 경기도,전라도,세종,제주도 지역 외에는, 모두 빨강(국민의힘)을 지지하였음')
    st.write('+ 분석1')
    st.write('전통적인 지역별 성향 차이로 인해, 전라도는 유독 파란색(민주당)이며, 경상도는 유독 빨간색(국민의힘)임.')
    st.write('+ 분석2')
    st.write('나머지 지역들은, 새빨갛거나,새파란 지역이 없음 > 경상도,전라도 외엔 정치적 성향이 없는 편임')

st.write('### 계엄 이후 민주당 지지율 증감')

gu_map_sido = folium.Map(location = [37.541, 126.986], #서울 중심부 시작
                         zoom_start = 7,
                         tiles='cartodbpositron')

folium.Choropleth(
    geo_data = gdf_korea_sido,
    data = df_homeprice,
    columns = ('분류.1','계엄 이후 민주당 지지율 증감'),
    key_on = 'feature.properties.시도별',
    fill_color = 'RdBu',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '민주당 지지도 변화율'
).add_to(gu_map_sido)

folium_static(gu_map_sido)

if st.button('해석 및 분석 보기2'):
    st.write('+ 해석')
    st.write('비상 계엄 사태 이후로, 경상도를 제외한 모든 지역이 민주당 지지율이 올라갔음')
    st.write('+ 분석')
    st.write('지역적 정치 성향이 있는 경상도 외에는, 이번 비상 계엄 사태를, 큰 잘못으로 생각하는듯 함.')


st.write('### 최근 달러 환율 변화')
st.write('##### 확대해서 보세요!!! (y값 범위를 따로 지정할 수가 없었습니다)')

df_dollar_yoon = pd.DataFrame(
    {
        "월별": ['올해10월','올해11월','올해12월','2024.7월','2024.8월','2024.9월'],
        "달러환율": [1370,1400,1440,1380,1350,1320]
    }
)

st.line_chart(
    df_dollar_yoon,
    x="월별",
    y="달러환율"
    )

if st.button('데이터 확인 해보기1'):
    st.dataframe(df_dollar_yoon)

col_1, col_2 = st.columns([1,1])

col_1.write('##### 2024년 8월')
col_1.write('+ 엔캐리 청산 사건 발생')
col_1.write('일본의 기준 금리가 올라가면서 수익이 감소할 것으로 예상되니 투자자가 자산을 팔아 본국으로 투자금을 회수')
col_1.write('이에 따라 달러 폭락 발생')


col_2.write('##### 2024년 12월')
col_2.write('+ 윤석열 비상 계엄 선포')
col_2.write('대한민국 원화 위험도를 우려해, 많은 사람들이 안전자산인 달러로 몰림')
col_2.write('이에 따라 달러 폭등 발생')


st.write('### 박근혜 사건 당시 달러 환율 변화')
st.write('##### 확대해서 보세요!!! (y값 범위를 따로 지정할 수가 없었습니다)')

df_dollar_park = pd.DataFrame(
    {
        "월별": ['2016년10월','2016년11월(최순실게이트)','2016년12월','2017년1월','2017년2월','2017년3월(탄핵)'],
        "달러환율": [1120,1160,1182,1200,1130,1150]
    }
)

st.line_chart(
    df_dollar_park,
    x="월별",
    y="달러환율"
    )

if st.button('데이터 확인 해보기2'):
    st.dataframe(df_dollar_park)

col_1, col_2 = st.columns([1,1])

col_1.write('##### 2016년 11월')
col_1.write('+ 최순실 국정농단 밝혀짐')
col_1.write('대한민국 정치적 불안정이, 경제적 위험을 야기하며, 안전자산인 달러로 몰림')
col_1.write('이에 따라 달러 환율 점점 증가')


col_2.write('##### 2017년 3월')
col_2.write('+ 박근혜 탄핵')
col_2.write('몇개월간 탄핵이 추진되면서, 결국 탄핵되고, 다시 정치적 안정이 찾아옴')
col_2.write('정치적 안정으로 원화도 안정')


gu_map_sido = folium.Map(location = [37.541, 126.986], #서울 중심부 시작
                         zoom_start = 7,
                         tiles='cartodbpositron')

st.write('### 2016년 당시 지역별 평당 집값(만원 단위)')

folium.Choropleth(
    geo_data = gdf_korea_sido,
    data = df_homeprice,
    columns = ('분류.1','2016년 9월'),
    key_on = 'feature.properties.시도별',
    fill_color = 'OrRd',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '평당 집값(만원)'
).add_to(gu_map_sido)

folium_static(gu_map_sido)

if st.button('지역별 집값 데이터 보기'):
    st.dataframe(df_homeprice[['분류.1','2016년 9월']])

st.write('### 최순실 사건 전후, 지역별 평당 집값 증감(만원단위)')

gu_map_sido = folium.Map(location = [37.541, 126.986], #서울 중심부 시작
                         zoom_start = 7,
                         tiles='cartodbpositron')

folium.Choropleth(
    geo_data = gdf_korea_sido,
    data = df_homeprice,
    columns = ('분류.1','최순실 사건 전후, 가격 차이(만원)'),
    key_on = 'feature.properties.시도별',
    fill_color = 'RdYlGn',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '평당 가격 증감(만원)'
).add_to(gu_map_sido)

folium_static(gu_map_sido)

col_1, col_2 = st.columns([1,1])

col_1.write('##### 수도권 및 도시')
col_1.write('+ 서울,경기도,대구 등')
col_1.write('수도권 및 도시둘은, 국정농단 사건으로, 평당 집값에 큰 타격을 입음')
col_1.dataframe(df_homeprice.loc[[3,9,10,16],['분류.1','최순실 사건 전후, 가격 차이(만원)']])


col_2.write('##### 비도시지역')
col_2.write('+ 나머지 지역들')
col_2.write('나머지 지역들은, 가격이 크게 빠지지 않았고, 오히려 대부분 올랐음')
col_2.dataframe(df_homeprice.loc[[11,12,13,14,15,17,18,19,20,21,22,23],['분류.1','최순실 사건 전후, 가격 차이(만원)']])

st.write('##### 해석')
st.write('+ 도시 지역들은, 장사 목적으로 집을 구매하는 경우가 많기 때문에, 집값에 타격이 심하였고,')
st.write('+ 비도시 지역들은, 대부분 주거 목적으로 집을 구매하기 때문에, 큰 타격이 없는 것으로 보임')

st.write('##### 사건 전후, 집값의 변화 정도를 퍼센트(%)로 확인해보자')
st.write('### 지역별 평당 집값 증감률(%): 사건 터지기 전 대비한 증감율')


gu_map_sido = folium.Map(location = [37.541, 126.986], #서울 중심부 시작
                         zoom_start = 7,
                         tiles='cartodbpositron')

folium.Choropleth(
    geo_data = gdf_korea_sido,
    data = df_homeprice,
    columns = ('분류.1','사건 전후, 가격 차이(%)'),
    key_on = 'feature.properties.시도별',
    fill_color = 'RdYlGn',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '평당 가격 증감률(%)'
).add_to(gu_map_sido)

folium_static(gu_map_sido)

st.write('증감률(%)로 확인해보니, 지역별로 집값이 얼마나 빠졌는지 더 직관적')

col_1, col_2 = st.columns([1,1])

col_1.write('##### 수도권 및 도시')
col_1.write('+ 서울,경기도,대구 등')
col_1.dataframe(df_homeprice.loc[[3,9,10,16],['분류.1','사건 전후, 가격 차이(%)']])
col_1.write('특히, 서울,대구는 한달만에 약 4% 빠졌고')
col_1.write('경기도는 한달만에 5% 가까이 빠짐')


col_2.write('##### 비도시지역')
col_2.write('+ 나머지 지역들')
col_2.dataframe(df_homeprice.loc[[11,12,13,14,15,17,18,19,20,21,22,23],['분류.1','사건 전후, 가격 차이(%)']])
col_2.write('비도시지역들은 대부분이 오히려 올랐음')

st.write("### 총 정리 및 통찰")
col_1, col_2,col_3 = st.columns([1,1,1])
col_1.write('##### 계엄 이후 지지율 변화')
col_1.write('+ 계엄 이후, 경상도를 제외한 대부분의 지역에서 국민의힘 지지도가 떨어지고, 민주당의 지지도가 오름')
col_1.write('+ 따라서 이번에 다시 탄핵이 되든 안되든, 다음 대통령은 민주당이 유력할 것으로 유추해볼 수 있음')

col_2.write('##### 달러 환율 변화')
col_2.write('+ 박근혜 탄핵 전에, 정치적 불안정이, 단기적인 환율 상승을 초래하였음')
col_2.write('+ 하지만, 탄핵 후에, 정치적인 안정이 찾아오면, 달러 환율이 다시 안정되었음.')
col_2.write('+ 이번에도, 정치적 불안정(계엄)으로 폭등한 달러 환율이, 정치적으로 다시 안정되면, 다시 안정화될 것으로 기대해볼 수 있음')

col_3.write('##### 지역별 집값 변화')
col_3.write('+ 박근혜 사건 당시, 수도권 집값은 단기적으로 폭락하였고, 비도시지역은 큰 타격이 없었음')
col_3.write('+ 이번에도 마찬가지로, 비슷하게 기대해볼 수 있음')