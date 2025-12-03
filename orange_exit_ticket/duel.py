import streamlit as st
import random

st.set_page_config(page_title="Duel", page_icon="⚔️")

# ----------------------------
# Initialize Session State
# ----------------------------
if "player_health" not in st.session_state:
    st.session_state.player_health = 50
if "enemy_health" not in st.session_state:
    st.session_state.enemy_health = 50
if "enemy_name" not in st.session_state:
    st.session_state.enemy_name = random.choice(["Goblin", "Skeleton", "Orc"])
if "round_result" not in st.session_state:
    st.session_state.round_result = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "selected_attack" not in st.session_state:
    st.session_state.selected_attack = None

# Hint system state
if "enemy_hint" not in st.session_state:
    st.session_state.enemy_hint = ""
if "real_enemy_choice" not in st.session_state:
    st.session_state.real_enemy_choice = ""
if "hint_generated" not in st.session_state:
    st.session_state.hint_generated = False


# ----------------------------
# Reset Game
# ----------------------------
def reset_game():
    st.session_state.player_health = 50
    st.session_state.enemy_health = 50
    st.session_state.enemy_name = random.choice(["Goblin", "Skeleton", "Orc"])
    st.session_state.round_result = ""
    st.session_state.game_over = False
    st.session_state.selected_attack = None
    st.session_state.enemy_hint = ""
    st.session_state.real_enemy_choice = ""
    st.session_state.hint_generated = False


# ----------------------------
# Determine Attack Outcome
# ----------------------------
def determine_round_result(player, enemy):
    if player == enemy:
        return "tie"

    win_map = {
        "High Strike": "Low Strike",
        "Medium Strike": "High Strike",
        "Low Strike": "Medium Strike"
    }

    if win_map[player] == enemy:
        return "win"
    return "lose"


# ----------------------------
# Hint Generation
# ----------------------------
def generate_enemy_choice_and_hint():
    st.session_state.real_enemy_choice = random.choice(
        ["High Strike", "Medium Strike", "Low Strike"]
    )

    # 70% truthful, 30% trick
    if random.random() < 0.7:
        st.session_state.enemy_hint = st.session_state.real_enemy_choice
    else:
        fake = ["High Strike", "Medium Strike", "Low Strike"]
        fake.remove(st.session_state.real_enemy_choice)
        st.session_state.enemy_hint = random.choice(fake)

    st.session_state.hint_generated = True


# ----------------------------
# MAIN UI
# ----------------------------
st.title("⚔️ Duel")

with st.expander("📘 How to Play"):
    st.write("""
**Welcome to Duel!**

This game works like **Rock–Paper–Scissors**, but with weapon attacks:

- **High Strike** = Rock  
- **Medium Strike** = Paper  
- **Low Strike** = Scissors  

**What beats what:**
- High Strike **beats** Low Strike  
- Medium Strike **beats** High Strike  
- Low Strike **beats** Medium Strike  

**Battle Rules:**
- You and the enemy start with **50 health**.
- Losing a round deals **5–10 damage**.
- Matching attacks causes **no damage**.
- Reduce the enemy to **0 HP** to win!
    """)

# ----------------------------
# Health Bars
# ----------------------------
st.write(f"**Your Health:** {st.session_state.player_health}/50")
st.progress(st.session_state.player_health / 50)

st.write(f"**Enemy ({st.session_state.enemy_name}) Health:** {st.session_state.enemy_health}/50")
st.progress(st.session_state.enemy_health / 50)

st.divider()

# ----------------------------
# End Screen
# ----------------------------
if st.session_state.game_over:
    if st.session_state.player_health <= 0:
        st.error("💀 You have been defeated...")
    else:
        st.success(f"🏆 You defeated the {st.session_state.enemy_name}!")

    if st.button("Play Again"):
        reset_game()
        st.rerun()

    st.stop()

# ----------------------------
# Generate Hint
# ----------------------------
if not st.session_state.hint_generated:
    generate_enemy_choice_and_hint()

with st.expander("🔮 Show Hint"):
    st.write(f"The enemy *might* be preparing: **{st.session_state.enemy_hint}**")
    st.caption("(This hint may be truthful or a trick!)")

st.divider()

# ----------------------------
# Attack Selection
# ----------------------------
attack_choice = st.radio(
    "Choose your attack:",
    ["High Strike", "Medium Strike", "Low Strike"],
    index=0
)

if st.button("Confirm Attack"):
    st.session_state.selected_attack = attack_choice

    player_attack = st.session_state.selected_attack
    enemy_attack = st.session_state.real_enemy_choice

    outcome = determine_round_result(player_attack, enemy_attack)

    if outcome == "tie":
        st.session_state.round_result = (
            f"Tie! Both used **{player_attack}**."
        )
    elif outcome == "win":
        dmg = random.randint(5, 10)
        st.session_state.enemy_health -= dmg
        st.session_state.round_result = (
            f"Your **{player_attack}** beat the enemy's **{enemy_attack}**!\n"
            f"The enemy took **{dmg} damage**."
        )
    else:
        dmg = random.randint(5, 10)
        st.session_state.player_health -= dmg
        st.session_state.round_result = (
            f"The enemy's **{enemy_attack}** beat your **{player_attack}**!\n"
            f"You took **{dmg} damage**."
        )

    if st.session_state.player_health <= 0 or st.session_state.enemy_health <= 0:
        st.session_state.game_over = True

    st.session_state.selected_attack = None
    st.session_state.hint_generated = False

    st.rerun()

# ----------------------------
# Round Result Message
# ----------------------------
if st.session_state.round_result:
    st.info(st.session_state.round_result)
