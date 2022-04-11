from tarfile import PAX_FIELDS
from matplotlib.pyplot import title
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px


st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpl6jZiw_dDRRnb1zPYGdk6zIVl-TRuWWHng&usqp=CAU", width=100)
st.title("Data Exploration Analysis App")
st.text('''The main purpose of this app is to provide the user facility to draw charts easily. 
As we know in data exploration analysis there are different types of charts, every chart has 
its own requirements like a histogram and scatter chart only best for the columns of the numerical 
type. if you try to visualize the categorical in scatter then it will through an error message. 
To overcome this problem this app will automatically split the categorical and numerical columns 
and will help you, it will show those columns of the dataset which are the requirements of the 
chart type.  
''')

#import dataset
#How to upload a file from pc
with st.sidebar.header("upload your dataset(.csv)"):
    upload_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df= sns.load_dataset('titanic')

#profiling report for pandas
if upload_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(upload_file)
        return csv
    df = load_csv()
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
else:
    st.info('Awaiting for CSV file, Please upload ')
    if st.button('Press to use example data'):
        #example dataset
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5),
                            columns=['age', 'banana', 'codanic','Duetchland','Ear'])
            return a
        df = load_data()
         


#summary stat
st.markdown('**summary statistic**')
st.write(df.describe())

col_sel = df.columns
#st.write(col_sel)
#col_opt = st.selectbox('Select Columns which you want to visulaize', col_sel)

num_vars = df.select_dtypes(include=['int64', 'float64']).columns
cat_vars = df.select_dtypes(include=['O']).columns

st.markdown('**These are the Categorical columns(string, bolean)**')
st.write(cat_vars)
st.markdown('**These are the Numerical columns(Int, float)**')
st.write(num_vars)
st.text('The Above columns spliting will help you to visualize a proper plot')

#ploting option
plot_list = st.selectbox('Select Columns which you want to visulaize',['select','Histogram','Bar-Chart','Scatter'] ,0)
#Histogram plot
if plot_list == 'Histogram':
    fig = px.histogram(df, x=st.selectbox('select x',num_vars, 0), title=st.text_input('Chart title (Histogram)'))
    st.write(fig)

#bar plot
elif plot_list == 'Bar-Chart':
    fig = px.bar(df, x=st.selectbox('Select x', col_sel, 0), y=st.selectbox('Select y', col_sel, 0 ), 
    color=st.selectbox('Select color', col_sel, 0), text_auto=True, title=st.text_input('Chart title(Bar-chart)'))
    st.write(fig)
#scatter plot
elif plot_list == 'Scatter':
    fig = px.scatter(df, x=st.selectbox('select x',num_vars), y=st.selectbox('select y',num_vars), 
                 size = st.selectbox('select size',num_vars), color=st.selectbox('select color',cat_vars), 
                 hover_name=st.selectbox('select hover-name',cat_vars),
                 log_x=True, size_max=55, range_x=[100, 100000], range_y=[20, 90], title=st.text_input('Chart title (Scatter)'))
    st.write(fig)
else:
    print('chose proper chart')

