class MoodCard extends HTMLElement {
  set hass(hass) {
    if (!this.card) {
      const card = document.createElement("ha-card");
      this.card = card;
      this.appendChild(card);
      if (this.card.shadowRoot && this.card.shadowRoot.host) {
        console.log("Mood card: Updating shadow root");
        this.card.shadowRoot.host.style.color = "#000";
      } else {
        console.log("Mood card: Could not find shadow root");
      }

      this.setBackground = rgb => (card.shadowRoot.host.style.background = rgb);
      this.setTitle = title => {
        card.header = title;
        const header = card.shadowRoot.querySelector(".card-header");
        if (header) {
          header.style.padding = "1em 16px";
        }
      };
    }

    const entityId = this.config.entity;
    const state = hass.states[entityId];
    const stateStr = state ? state.state : "unavailable";

    if (stateStr.indexOf("(") === 0) {
      const rgb = stateStr;
      this.setBackground(`rgb${rgb}`);
      this.setTitle(rgb.replace("(", "").replace(")", ""));
    } else {
      this.setTitle("");
      this.setBackground("transparent");
    }
  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error("You need to define an entity");
    }
    this.config = config;
  }

  // The height of your card. Home Assistant uses this to automatically
  // distribute all cards over the available columns.
  getCardSize() {
    return 3;
  }
}

customElements.define("mood-card", MoodCard);
