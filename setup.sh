mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \amitparmar.it@charusat.ac.in\"\n\
" >~/.sreamlit/credentials.toml
echo"\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml