import streamlit as st
from rdkit import Chem
from rdkit.Chem import SanitizeMol

st.title("Comparación de Moléculas SMILES")
st.write("Autor: Jesus Alvarado-Huayhuaz")
st.markdown("Ingrese dos SMILES para verificar si corresponden a la misma molécula.")

# Entradas de SMILES
smiles1 = st.text_input("Ingrese el primer SMILES:", value="C1=CN=C(C=N1)C(=O)N")
smiles2 = st.text_input("Ingrese el segundo SMILES:", value="O=C(N)c1nccnc1")

# Función para sanitizar y convertir SMILES a Mol
def sanitize_and_convert(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)  # Convertir SMILES a Mol
        if mol:
            SanitizeMol(mol)  # Sanitizar la molécula
            return mol
        else:
            return None
    except Exception as e:
        return None

# Procesar las moléculas
if st.button("Comparar moléculas"):
    mol1 = sanitize_and_convert(smiles1)
    mol2 = sanitize_and_convert(smiles2)

    if mol1 and mol2:
        # Comparar utilizando fingerprints
        is_same = mol1.HasSubstructMatch(mol2) and mol2.HasSubstructMatch(mol1)
        st.subheader("Resultados de la Comparación:")
        if is_same:
            st.success("Las moléculas son equivalentes.")
        else:
            st.error("Las moléculas no son equivalentes.")
    else:
        st.error("Una o ambas entradas no son SMILES válidos. Verifique los datos ingresados.")

# Notas adicionales
#st.markdown(
#    """
#    **Notas:**
#    - La sanitización corrige errores comunes en los SMILES ingresados.
#    - La equivalencia molecular se determina considerando la estructura química.
#    """
#)
