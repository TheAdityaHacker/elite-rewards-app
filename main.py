import flet as ft

def main(page: ft.Page):
    page.title = "ELITE REWARDS PRO"
    page.bgcolor = "black"
    page.padding = 30
    page.horizontal_alignment = "center"
    
    balance = ft.Text("$0.00", size=45, weight="bold", color="#FFD700")

    def btn_click(e):
        current_val = float(balance.value.replace("$", ""))
        new_val = current_val + 0.10
        balance.value = f"${new_val:.2f}"
        
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Ad Loaded! $0.10 Added to your Wallet"),
            bgcolor="#39FF14"
        )
        page.snack_bar.open = True
        page.update()

    page.add(
        ft.Container(height=20),
        ft.Text("ELITE REWARDS", size=30, color="#39FF14", weight="bold"),
        ft.Divider(color="grey"),
        ft.Text("Available Balance", size=14, color="grey"),
        balance,
        ft.Container(height=40),
        
        ft.ElevatedButton(
            content=ft.Container(
                content=ft.Text("WATCH AD & EARN", color="black", weight="bold"),
                padding=10
            ),
            bgcolor="#39FF14",
            on_click=btn_click,
            width=300,
            height=60,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            )
        ),
        ft.Container(height=20),
        ft.Text("Click the button to see the magic!", color="grey", size=12)
    )
    
    page.update()

if __name__ == "__main__":
    ft.run(main)
