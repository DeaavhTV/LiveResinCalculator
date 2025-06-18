import streamlit as st

st.set_page_config(page_title="Vape Batch Calculator", layout="centered")

st.title("🧪 Vape Batch Calculator")

tab1, tab2, tab3 = st.tabs(["📊 Ratio Checker", "🧪 Dilution Calculator", "📜 Credits"])


with tab1:
    st.markdown("### 🧫 Batch Input")
    st.markdown("Enter number of carts to be made, amount of grams per cart and the amount of strains you are working with.")


    # Inputs
    num_carts = st.number_input("Number of Carts", min_value=1, value=43)
    grams_per_cart = st.number_input("Grams per Cart", min_value=0.1, value=4.0, step=0.1)
    num_strains = st.number_input("Number of Strains", min_value=1, value=5)

    st.markdown("### ⚖️ Component Ratios (must total 100%)")
    dist_pct = st.slider("Distillate %", 0, 100, 60)
    resin_pct = st.slider("Live Resin %", 0, 100, 35)
    terp_pct = st.slider("Terpenes %", 0, 100, 5)

    total_pct = dist_pct + resin_pct + terp_pct
    error = False

    if total_pct != 100:
        st.error(f"❌ Ratios must total 100%. Your current total is {total_pct}%.")
        diff = 100 - total_pct
        if diff > 0:
            st.info(f"🔧 Add {diff}% more across components.")
        else:
            st.info(f"🔧 Remove {-diff}% across components.")
        error = True

    if not error:
        total_mass = num_carts * grams_per_cart

        # Compute total amounts
        total_dist = total_mass * (dist_pct / 100)
        total_resin = total_mass * (resin_pct / 100)
        total_terps = total_mass * (terp_pct / 100)

        # Per strain
        strain_mass = total_mass / num_strains
        strain_dist = strain_mass * (dist_pct / 100)
        strain_resin = strain_mass * (resin_pct / 100)
        strain_terps = strain_mass * (terp_pct / 100)

        st.markdown("### 🧾 Batch Totals")
        st.write(f"**Total Mix Weight:** {total_mass:.2f}g")
        st.write(f"- Distillate: {total_dist:.2f}g")
        st.write(f"- Live Resin: {total_resin:.2f}g")
        st.write(f"- Terpenes: {total_terps:.2f}g")

        st.markdown("### 🌿 Per Strain Breakdown")
        st.write(f"**Each Strain Batch:** {strain_mass:.2f}g")
        st.write(f"- Distillate: {strain_dist:.2f}g")
        st.write(f"- Live Resin: {strain_resin:.2f}g")
        st.write(f"- Terpenes: {strain_terps:.2f}g")

with tab2:
    st.title("💧 Dilution Calculator")
    st.markdown("Estimate how much of your final mix is made up of **non-THC resin components** and **total terpene content**.")

    st.markdown("### 🧬 Resin Composition")
    thc_pct = st.number_input("Live Resin THC %", 0.0, 100.0, 60.0)
    terp_sauce_pct = st.number_input("Terp Sauce / Waxes / Lipids % in Resin", 0.0, 100.0, 40.0)
    total_resin_content = thc_pct + terp_sauce_pct

    if total_resin_content > 100:
        st.error(f"❌ Resin composition exceeds 100% ({total_resin_content}%). Please adjust.")
    else:
        st.markdown("### ⚗️ Batch Details")
        resin_used_pct = st.slider("Live Resin used in Batch (%)", 0, 100, 35)
        batch_mass = st.number_input("Total Batch Mass (g)", min_value=0.1, value=172.0)
        extra_terps_pct = st.slider("Extra Terpenes added to Batch (%)", 0, 20, 5)

        # Mass Calculations
        resin_mass = batch_mass * resin_used_pct / 100
        terp_mass_from_resin = resin_mass * terp_sauce_pct / 100
        terp_mass_from_added = batch_mass * extra_terps_pct / 100
        total_terp_mass = terp_mass_from_resin + terp_mass_from_added

        dilution = (terp_mass_from_resin / batch_mass) * 100
        final_terp_pct = (total_terp_mass / batch_mass) * 100

        st.markdown("### 🧾 Results")
        st.write(f"- **Resin used:** {resin_mass:.2f}g ({resin_used_pct}%)")
        st.write(f"- Terp Sauce from Resin: {terp_mass_from_resin:.2f}g")
        st.write(f"- Extra Terpenes added: {terp_mass_from_added:.2f}g")
        st.write(f"- **Total Terpenes in Final Batch:** {total_terp_mass:.2f}g")
        st.success(f"✅ Final Terpene Content: **{final_terp_pct:.2f}%** of total mix")
        st.info(f"🧊 Terp Sauce (non-THC) Dilution Alone: **{dilution:.2f}%**")

with tab3:
    st.title("📜 Credits")
    st.markdown("""
    **App Created by Deaavh**  
    Built with ❤️ using [Streamlit](https://streamlit.io/) and Python.  
    If this tool helped you, share it with others in the industry.
    """)