console.log("IN HERE");
class RainbowCard extends HTMLElement {
  set hass(hass) {
    if (!this.card) {
      const card = document.createElement("ha-card");
      card.shadowRoot.host.style.color = "#000";
      this.card = card;
      this.appendChild(card);

      this.setBackground = rgb => (card.shadowRoot.host.style.background = rgb);
      this.setTitle = title => {
        card.header = title;
        const header = card.shadowRoot.querySelector(".card-header");
        if (header) {
          header.style.padding = "1em 16px";
        }
      };
    }

    console.log("New hass", hass);
    console.log("Connecting");
    hass
      .callWS({
        type: "lovelace/colours",
      })
      .then(response => {
        console.log("Got response", response);
        this.setRainbows(response);
      });

    if (!this.rainbow) {
      // card.shadowRoot.host.style.color = "#000";
      this.rainbow = document.createElement("div");
      this.rainbow.style.display = "flex";
      this.rainbow.style.flexWrap = "wrap";
      this.rainbow.style.justifyContent = "space-evenly";
      this.appendChild(this.rainbow);
    }

    const currentIndex = hass.states["input_number.effect_index_key"].state;

    const formatColour = colour => {
      if (Array.isArray(colour)) {
        return `rgb(${colour.join(",")})`;
      }
      return colour;
    };

    this.setRainbows = colours => {
      this.rainbow.innerHTML = colours
        .map(function (each, index) {
          let style = `background: ${formatColour(
            each
          )}; display: inline-block; flex-grow: 4; min-width: 20px; height: 80px; `;
          if (currentIndex === index.toString()) {
            style += "; border: solid 2px white;";
          }
          return `<div style="${style}"></div>`;
        })
        .join("");
    };

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

    console.log("New hass", hass);
    // const colours = JSON.parse(hass.states["input_text.colours_json"].state);
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

customElements.define("rainbow-card", RainbowCard);
