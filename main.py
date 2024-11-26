import streamlit as st

# titulos
st.title("Titulo de nivel 1")
st.header("Título de nivel 2")
st.subheader("Título de nivel 3")

# textos
st.markdown("""
En una etiqueta tipo markdown pueden poner cualquier texto en el formato markdwon.
Podemos poner un texto en **negrilla**, en *italica* o en ***ambos***.

Esto es otra linea.

Enumeraciones:
1. Primer item
2. Segundo item
3. tercer item

Items:
+ Item 1
+ Item 2
+ Item 3

Podemos dar color al texto por ejemplo :red[rojo], :blue[azul], :green[verde] y :orange[así]...
""")

# ecuaciones
st.latex("a^2 + b^2 = c^2")

# elemento media:
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc9wEuFT-XY4L2RvxqKpV3j0gVKeAOzVRTGw&s")

st.video("https://www.youtube.com/watch?v=eTEBvBIz8Ok")