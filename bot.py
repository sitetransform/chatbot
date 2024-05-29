import streamlit as st
import os
import google.generativeai as genai

st.markdown("""
<style>
   *,
*:after,
*:before {
  box-sizing: inherit;
}

*[disabled] {
  cursor: not-allowed;
}

html {
  box-sizing: border-box;
  font-size: 62.5%;
}

body {
  font-family: 'Roboto', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
  font-size: 1.6em;
  font-weight: 300;
  letter-spacing: .01em;
  line-height: 1.6;
}

blockquote {
  border-left: 0.3rem solid #d1d1d1;
  margin-left: 0;
  margin-right: 0;
  padding: 1rem 1.5rem;
}

blockquote *:last-child {
  margin-bottom: 0;
}

.transbtn,
button,
input[type='button'],
input[type='reset'],
input[type='submit'] {
  background-color: royalblue;
  border: 0.1rem solid royalblue;
  border-radius: .4rem;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-size: 1.1rem;
  font-weight: 700;
  height: 3.8rem;
  letter-spacing: .1rem;
  line-height: 3.8rem;
  padding: 0 3.0rem;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  white-space: nowrap;
}

.transbtn:focus, .transbtn:hover,
button:focus,
button:hover,
input[type='button']:focus,
input[type='button']:hover,
input[type='reset']:focus,
input[type='reset']:hover,
input[type='submit']:focus,
input[type='submit']:hover {
  background-color: #213571;
  border-color: #213571;
  color: #fff;
  outline: 0;
}

.transbtn[disabled],
button[disabled],
input[type='button'][disabled],
input[type='reset'][disabled],
input[type='submit'][disabled] {
  opacity: .5;
}

.transbtn[disabled]:focus, .transbtn[disabled]:hover,
button[disabled]:focus,
button[disabled]:hover,
input[type='button'][disabled]:focus,
input[type='button'][disabled]:hover,
input[type='reset'][disabled]:focus,
input[type='reset'][disabled]:hover,
input[type='submit'][disabled]:focus,
input[type='submit'][disabled]:hover {
  background-color: royalblue;
  border-color: royalblue;
}

.transbtn-outline,
button.transbtn-outline,
input[type='button'].transbtn-outline,
input[type='reset'].transbtn-outline,
input[type='submit'].transbtn-outline {
  background-color: transparent;
  color: royalblue;
}

.transbtn-outline:focus, .transbtn-outline:hover,
button.transbtn-outline:focus,
button.transbtn-outline:hover,
input[type='button'].transbtn-outline:focus,
input[type='button'].transbtn-outline:hover,
input[type='reset'].transbtn-outline:focus,
input[type='reset'].transbtn-outline:hover,
input[type='submit'].transbtn-outline:focus,
input[type='submit'].transbtn-outline:hover {
  background-color: #213571;
  color: white;
}

.transbtn-outline[disabled]:focus, .transbtn-outline[disabled]:hover,
button.transbtn-outline[disabled]:focus,
button.transbtn-outline[disabled]:hover,
input[type='button'].transbtn-outline[disabled]:focus,
input[type='button'].transbtn-outline[disabled]:hover,
input[type='reset'].transbtn-outline[disabled]:focus,
input[type='reset'].transbtn-outline[disabled]:hover,
input[type='submit'].transbtn-outline[disabled]:focus,
input[type='submit'].transbtn-outline[disabled]:hover {
  border-color: inherit;
  color: royalblue;
}

.transbtn-clear,
button.transbtn-clear,
input[type='button'].transbtn-clear,
input[type='reset'].transbtn-clear,
input[type='submit'].transbtn-clear {
  background-color: transparent;
  border-color: transparent;
  color: royalblue;
}

.transbtn-clear:focus, .transbtn-clear:hover,
button.transbtn-clear:focus,
button.transbtn-clear:hover,
input[type='button'].transbtn-clear:focus,
input[type='button'].transbtn-clear:hover,
input[type='reset'].transbtn-clear:focus,
input[type='reset'].transbtn-clear:hover,
input[type='submit'].transbtn-clear:focus,
input[type='submit'].transbtn-clear:hover {
  background-color: #213571;
  border-color: transparent;
  color: white;
}

.transbtn-clear[disabled]:focus, .transbtn-clear[disabled]:hover,
button.transbtn-clear[disabled]:focus,
button.transbtn-clear[disabled]:hover,
input[type='button'].transbtn-clear[disabled]:focus,
input[type='button'].transbtn-clear[disabled]:hover,
input[type='reset'].transbtn-clear[disabled]:focus,
input[type='reset'].transbtn-clear[disabled]:hover,
input[type='submit'].transbtn-clear[disabled]:focus,
input[type='submit'].transbtn-clear[disabled]:hover {
  color: royalblue;
}

code {
  background: #f4f5f6;
  border-radius: .4rem;
  font-size: 86%;
  margin: 0 .2rem;
  padding: .2rem .5rem;
  white-space: nowrap;
}

pre {
  background: #f4f5f6;
  border-left: 0.3rem solid royalblue;
  overflow-y: hidden;
}

pre > code {
  border-radius: 0;
  display: block;
  padding: 1rem 1.5rem;
  white-space: pre;
}

hr {
  border: 0;
  border-top: 0.1rem solid #f4f5f6;
  margin: 3.0rem 0;
}

input[type='color'],
input[type='date'],
input[type='datetime'],
input[type='datetime-local'],
input[type='email'],
input[type='month'],
input[type='number'],
input[type='password'],
input[type='search'],
input[type='tel'],
input[type='text'],
input[type='url'],
input[type='week'],
input:not([type]),
textarea,
select {
  -webkit-appearance: none;
  background-color: transparent;
  border: 0.1rem solid #d1d1d1;
  border-radius: .4rem;
  box-shadow: none;
  box-sizing: inherit;
  height: 3.8rem;
  padding: .6rem 1.0rem .7rem;
  width: 100%;
  -webkit-transition: 0.6s box-shadow;
  transition: 0.6 box-shadow;
}

input[type='color']:focus,
input[type='date']:focus,
input[type='datetime']:focus,
input[type='datetime-local']:focus,
input[type='email']:focus,
input[type='month']:focus,
input[type='number']:focus,
input[type='password']:focus,
input[type='search']:focus,
input[type='tel']:focus,
input[type='text']:focus,
input[type='url']:focus,
input[type='week']:focus,
input:not([type]):focus,
textarea:focus,
select:focus {
  box-shadow: 0 0 5px royalblue;
  padding: 3px 0px 3px 3px;
  margin: 5px 1px 3px 0px;
  border: 1px solid royalblue;
  outline: 0;
}

select {
  background: url('data:image/svg+xml;utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 8" width="30"><path fill="blue" d="M0,0l6,8l6-8"/></svg>') center right no-repeat;
  padding-right: 3.0rem;
}

select:focus {
  background-image: url('data:image/svg+xml;utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 8" width="30"><path fill="blue" d="M0,8l6-8l6,8"/></svg>');
}

select[multiple] {
  background: none;
  height: auto;
}

textarea {
  min-height: 6.5rem;
}

label,
legend {
  display: block;
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: .5rem;
}

fieldset {
  border-width: 0;
  padding: 0;
}

input[type="checkbox"],
input[type="radio"] {
  display: inline;
}

.label-inline {
  display: inline-block;
  font-weight: normal;
  margin-left: .5rem;
}

.container {
  margin: 0 auto;
  max-width: 112.0rem;
  padding: 0 2.0rem;
  position: relative;
  width: 100%;
}

.row {
  display: flex;
  flex-direction: column;
  padding: 0;
  width: 100%;
}

.row.row-no-padding {
  padding: 0;
}

.row.row-no-padding > .column {
  padding: 0;
}

.row.row-wrap {
  flex-wrap: wrap;
}

.row.row-top {
  align-items: flex-start;
}

.row.row-bottom {
  align-items: flex-end;
}

.row.row-center {
  align-items: center;
}

.row.row-stretch {
  align-items: stretch;
}

.row.row-baseline {
  align-items: baseline;
}

.row .column {
  display: block;
  flex: 1 1 auto;
  margin-left: 0;
  max-width: 100%;
  width: 100%;
}

.row .column.column-offset-10 {
  margin-left: 10%;
}

.row .column.column-offset-20 {
  margin-left: 20%;
}

.row .column.column-offset-25 {
  margin-left: 25%;
}

.row .column.column-offset-33, .row .column.column-offset-34 {
  margin-left: 33.3333%;
}

.row .column.column-offset-40 {
  margin-left: 40%;
}

.row .column.column-offset-50 {
  margin-left: 50%;
}

.row .column.column-offset-60 {
  margin-left: 60%;
}

.row .column.column-offset-66, .row .column.column-offset-67 {
  margin-left: 66.6666%;
}

.row .column.column-offset-75 {
  margin-left: 75%;
}

.row .column.column-offset-80 {
  margin-left: 80%;
}

.row .column.column-offset-90 {
  margin-left: 90%;
}

.row .column.column-10 {
  flex: 0 0 10%;
  max-width: 10%;
}

.row .column.column-20 {
  flex: 0 0 20%;
  max-width: 20%;
}

.row .column.column-25 {
  flex: 0 0 25%;
  max-width: 25%;
}

.row .column.column-33, .row .column.column-34 {
  flex: 0 0 33.3333%;
  max-width: 33.3333%;
}

.row .column.column-40 {
  flex: 0 0 40%;
  max-width: 40%;
}

.row .column.column-50 {
  flex: 0 0 50%;
  max-width: 50%;
}

.row .column.column-60 {
  flex: 0 0 60%;
  max-width: 60%;
}

.row .column.column-66, .row .column.column-67 {
  flex: 0 0 66.6666%;
  max-width: 66.6666%;
}

.row .column.column-75 {
  flex: 0 0 75%;
  max-width: 75%;
}

.row .column.column-80 {
  flex: 0 0 80%;
  max-width: 80%;
}

.row .column.column-90 {
  flex: 0 0 90%;
  max-width: 90%;
}

.row .column .column-top {
  align-self: flex-start;
}

.row .column .column-bottom {
  align-self: flex-end;
}

.row .column .column-center {
  align-self: center;
}

@media (min-width: 40rem) {
  .row {
    flex-direction: row;
    margin-left: -1.0rem;
    width: calc(100% + 2.0rem);
  }
  .row .column {
    margin-bottom: inherit;
    padding: 0 1.0rem;
  }
}

a,
a:focus {
  color: royalblue;
  text-decoration: none;
}

a:hover {
  color: #213571;
}

dl,
ol,
ul {
  list-style: none;
  margin-top: 0;
  padding-left: 0;
}

dl dl,
dl ol,
dl ul,
ol dl,
ol ol,
ol ul,
ul dl,
ul ol,
ul ul {
  font-size: 90%;
  margin: 1.5rem 0 1.5rem 3.0rem;
}

ol {
  list-style: decimal inside;
}

ul {
  list-style: circle inside;
}

.transbtn,
button,
dd,
dt,
li {
  margin-bottom: 1.0rem;
}

fieldset,
input,
select,
textarea {
  margin-bottom: 1.5rem;
}

blockquote,
dl,
figure,
form,
ol,
p,
pre,
table,
ul {
  margin-bottom: 2.5rem;
}

table {
  border-spacing: 0;
  display: block;
  overflow-x: auto;
  text-align: left;
  width: 100%;
}

td,
th {
  border-bottom: 0.1rem solid #ccc;
  padding: 1.2rem 1.5rem;
}

td:first-child,
th:first-child {
  padding-left: 0;
}

td:last-child,
th:last-child {
  padding-right: 0;
}

@media (min-width: 40rem) {
  table {
    display: table;
    overflow-x: initial;
  }
}

b,
strong {
  font-weight: bold;
}

p {
  margin-top: 0;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 300;
  letter-spacing: -.1rem;
  margin-bottom: 2.0rem;
  margin-top: 0;
}

h1 {
  font-size: 4.6rem;
  line-height: 1.2;
}

h2 {
  font-size: 3.6rem;
  line-height: 1.25;
}

h3 {
  font-size: 2.8rem;
  line-height: 1.3;
}

h4 {
  font-size: 2.2rem;
  letter-spacing: -.08rem;
  line-height: 1.35;
}

h5 {
  font-size: 1.8rem;
  letter-spacing: -.05rem;
  line-height: 1.5;
}

h6 {
  font-size: 1.6rem;
  letter-spacing: 0;
  line-height: 1.4;
}

img {
  max-width: 100%;
}

.clearfix:after {
  clear: both;
  content: ' ';
  display: table;
}

.float-left {
  float: left;
}

.float-right {
  float: right;
}
</style>
""", unsafe_allow_html=True)

st.title("Gemini Chatbot")

os.environ['GOOGLE_API_KEY'] = "AIzaSyA8bBlkr7sk4kngCFK_bxygHC0clWnGubg"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Select the model
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello, how may I help you today?"
        }
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process and store Query and Response


def llm_function(query):
    response = model.generate_content(query)

    # Displaying the Assistant Message
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )


# Accept user input
query = st.chat_input("What's up?")

# Calling the Function when Input is Provided
if query:
    # Displaying the User Message
    with st.chat_message("user"):
        st.markdown(query)

    llm_function(query)
