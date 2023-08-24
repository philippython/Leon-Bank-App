from flet import *
from data import *
from helper import user_info, generate_initial

class AccountInformation(UserControl):

    def __init__(self, page: Page):
        self.page = page
        super().__init__()

    def dashboard(self, event):
        self.page.go("/dashboard")

    def update_profile(self, event):
        self.page.go("/update-account-information")

    def sign_out(self, event):
        self.page.go("/")

    def did_mount(self):
        users_data = self.page.client_storage.get('users')
        active_user = self.page.client_storage.get('active_user')

        full_name = user_info(users_data, active_user)['full_name']
        user_initials = generate_initial(full_name)

        self.account_details.content.leading.content.value = user_initials
        self.account_details.content.title.value = full_name

        self.update()

    def build(self):
        self.top = Container(
            margin= 20 ,
            content= Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Container(
                            alignment= alignment.top_left,
                            content = IconButton(
                                icon = icons.ARROW_BACK,
                                icon_color=colors.WHITE,
                                on_click = self.dashboard
                                ),
                            ),
                            Text("Account Settings", weight=FontWeight.W_500, size=15, color=colors.WHITE),  
                            Stack(
                                [
                                Container(
                                    alignment= alignment.center,
                                    border_radius= 10,
                                    bgcolor= colors.GREY_900,
                                    content= 
                                        IconButton(
                                            icon= icons.NOTIFICATIONS_NONE,
                                            icon_color= colors.WHITE
                                        ),
                                ),
                                Container(
                                    margin = margin.only(left=30),
                                    alignment = alignment.top_right,
                                    content = CircleAvatar(bgcolor=GREEN_COLOR, radius=5)
                                )
                                ]
                            )
                        ]
            )
        )

        self.account_details = Container(
            margin= 10,
            border= border.all(1, colors.GREY_500),
            on_click= self.update_profile,
            content= ListTile(
                leading= CircleAvatar(
                    # foreground_image_url=AVATAR_IMAGE_URL
                    content= Text(value="FF", size=15, color = colors.GREY_500)
                ),
                title=Text("Odulaja Philip Temitayo", color=colors.WHITE, size=13),
                subtitle=Text("Account Details", color= colors.GREY_400, size=12),
                trailing= Icon(icons.ARROW_FORWARD_IOS_OUTLINED, color= colors.GREY_500)
            )
        )

        self.sign_out_text = Container(
            margin= 50,
            on_click= self.sign_out,
            content = Text(
                "sign out",
                color = colors.RED
            )
        )

        self.settings_control = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls= [
                self.top,
                self.account_details,
                self.sign_out_text
            ]
        )

        
        return self.settings_control