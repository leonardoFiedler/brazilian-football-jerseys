import streamlit as st
import gettext
_ = gettext.gettext

language = st.sidebar.selectbox(_("Language"), ['en', 'pt'])

dt_format = '%d/%M/%Y' if language == 'pt' else '%Y/%M/%d'

localizator = gettext.translation('messages', localedir='app/analytics/locales', languages=[language])
localizator.install()
_ = localizator.gettext


st.text(_("Language"))