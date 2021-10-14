import glob
import re
from collections import defaultdict
from typing import Any, Dict, List

import matplotlib.pyplot as plt

from GeneratePDF import WhatsAppReport

MESSAGE_PATTERN = re.compile(
    r"(\d+\/\d+\/\d+),\s.*-\s([^:]+):\s(.*)"
)  # date, sender, message of actual messages, not whatsapp events


class WhatsAppAnalyzer:
    def __init__(self) -> None:
        self.file_name = glob.glob("./WhatsApp*.txt")
        self.x = []
        self.y = []
        self.totalMessages = 0

    def chats_(self) -> List[str]:
        chat = open(self.file_name[0], "r", encoding="utf-8")
        chats = chat.readlines()
        chat.close()
        return chats

    def parse_info(self) -> Dict[str, int]:
        """Convert the text file into a dictionary of dates and number of messages"""

        data = defaultdict(lambda: 0)
        chats = self.chats_()
        for line in chats:
            a = re.findall(MESSAGE_PATTERN, line)
            if a:
                date, _, _ = a[0]
                data[date] += 1
        return data

    def plot_info(self) -> Dict[str, Any]:
        n = 0
        data = self.parse_info()
        for i in data:
            self.y.append(n)
            self.x.append(data[i])
            self.totalMessages += data[i]
            n += 1

        Keymax = max(data, key=data.get)

        # fig = plt.figure()
        # fig.suptitle(file_name, fontsize=14, fontweight='bold')
        # ax = fig.add_subplot(111)
        fig, ax = plt.subplots(1, 1)
        plt.subplots_adjust(top=0.85)

        # ax.set_title('total number of messages are {.} in {.} days. Average {.} text/day. On {} max number of text were sent:{}'.format(totalMessages,totalDays,totalMessages//len(data),Keymax,data[Keymax]))
        ax.plot(self.y, self.x)
        ax.set_xlabel("days$ \longrightarrow $")
        ax.set_ylabel("number of messages$ \longrightarrow $")

        data = {
            "totalMessages": self.totalMessages,
            "totalDays": len(data),
            "averageTextPerDay": self.totalMessages // len(data),
            "maxTextDate": Keymax,
            "maxTextOneDay": data[Keymax],
        }
        # print(data)
        # plt.show()
        # D = data
        # plt.bar(range(len(D)), list(D.values()), align='center')
        # plt.xticks(range(len(D)), list(D.keys()))
        # plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode
        # plt.show()

        plt.savefig("message-graph.png")
        # plt.close()
        return data

    def generate_pdf(self) -> None:
        data = self.plot_info()
        report = WhatsAppReport(data)
        report.generate()


if __name__ == "__main__":
    wa = WhatsAppAnalyzer()
    wa.generate_pdf()
