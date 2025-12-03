import streamlit as st
import random

# ---------------------------------------------
# Helper Functions
# ---------------------------------------------

def get_enemy():
    return random.choice(["Goblin", "Skeleton", "Orc"])

def get_damage():
    return random.randint(5, 10)

def determine_winner(player, enemy):
    # Mapping of who beats who
    beats = {
        "High Strike": "Low Strike",       # Rock beats Scissors
        "Medium Strike": "High Strike",    # Paper beats Rock
        "Low Strike": "Medium Strike"      # Scissors beats Paper
    }

    if player == enemy:
        return "tie"

    if beats[player] == enemy:
        return "player"
    else:
        return "enemy"

# ---------------------------------------------
# Session State Initialization
# ---------------------------------------------
if "player_health" not in st.session_state:
    st.session_state.player_health = 100

if "enemy_health" not in st.session_state:
    st.session_state.enemy_health = 100

if "enemy_name" not in st.session_state:
    st.session_state.enemy_name = get_enemy()

if "round_result" not in st.session_state:
    st.session_state.round_result = ""

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# ---------------------------------------------
# Game Reset Function
# ---------------------------------------------
def reset_game():
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.enemy_name = get_enemy()
    st.session_state.round_result = ""
    st.session_state.game_over = False

# ---------------------------------------------
# UI Layout
# ---------------------------------------------

st.title("⚔️ DUEL: A Rock-Paper-Scissors Battle")

st.subheader("How to Play")
st.markdown("""
Welcome to **Duel**, a fantasy battle inspired by Rock-Paper-Scissors!

### ⚔ Strike Types  
- **High Strike** beats **Low Strike**  
- **Medium Strike** beats **High Strike**  
- **Low Strike** beats **Medium Strike**

### ❤️ Health System  
- You and your opponent each start with **100 health**  
- Lose a round → take **5–10 damage**  
- Tie → no damage  
- First to reach **0 health** loses!
""")

st.divider()

# Health Display
col1, col2 = st.columns(2)
with col1:
    st.metric("Your Health", st.session_state.player_health)
with col2:
    st.metric(f"{st.session_state.enemy_name}'s Health", st.session_state.enemy_health)

st.divider()

# ---------------------------------------------
# If Game Over
# ---------------------------------------------
if st.session_state.game_over:
    if st.session_state.player_health <= 0:
        st.error("💀 You have been defeated...")
    else:
        st.success(f"🏆 You defeated the {st.session_state.enemy_name}!")

    st.button("Play Again", on_click=reset_game)
    st.stop()

# ---------------------------------------------
# Player Move Buttons
# ---------------------------------------------
st.subheader("Choose your strike:")

moves = ["High Strike", "Medium Strike", "Low Strike"]
cols = st.columns(3)

for i, move in enumerate(moves):
    if cols[i].button(move):
        enemy_move = random.choice(moves)
        winner = determine_winner(move, enemy_move)

        if winner == "player":
            damage = get_damage()
            st.session_state.enemy_health -= damage
            st.session_state.round_result = (
                f"🗡️ You used **{move}**. {st.session_state.enemy_name} used **{enemy_move}**.\n"
                f"🎯 You hit the enemy for **{damage} damage!**"
            )
        elif winner == "enemy":
            damage = get_damage()
            st.session_state.player_health -= damage
            st.session_state.round_result = (
                f"🗡️ You used **{move}**. {st.session_state.enemy_name} used **{enemy_move}**.\n"
                f"💥 You took **{damage} damage!**"
            )
        else:
            st.session_state.round_result = (
                f"🤝 Both used **{move}** — it's a tie! No damage dealt."
            )

        # Check for win/lose
        if st.session_state.player_health <= 0 or st.session_state.enemy_health <= 0:
            st.session_state.game_over = True

        st.rerun()

# Display Round Results
if st.session_state.round_result:
    st.info(st.session_state.round_result)
