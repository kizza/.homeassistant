const parseResults = (res) => res.json().then((json) => json[0]);

const fetchHistory = (_entity, token) =>
  fetch(
    `/api/history/period?filter_entity_id=binary_sensor.lumi_extra_motion`,
    {
      method: "get",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

const filterToActive = (values) => values.filter((each) => each.state === "on");

const mapToLocalTimezone = (values) => {
  const tzOffset = new Date().getTimezoneOffset() * 6000;

  return values.map((each) => {
    const timestamp = new Date(each.last_updated) + tzOffset;
    const localised = new Date(timestamp.split("(")[0]);
    return {
      ...each,
      timestamp: localised,
    };
  });
};

const filterToThisMorning = (values) => {
  const date = new Date().getDate();
  return values.filter(
    ({ timestamp }) => timestamp.getDate() === date && timestamp.getHours() <= 7
  );
};

const formatItems = (items) =>
  items.map((each) => each.timestamp.toLocaleString("en-US").split(", ")[1]);

const getHistory = (entity, token) =>
  fetchHistory(entity, token)
    .then(parseResults)
    .then(filterToActive)
    .then(mapToLocalTimezone)
    .then(filterToThisMorning)
    .then(formatItems)
    .catch((e) => console.log("Error getting history", e));

const asList = (innerHTML) =>
  `<ul style="list-style-type:none; padding:0; margin:0">${innerHTML}<div style="clear: both"></div></ul>`;

const asListItem = (innerHTML) => {
  const [timestamp, am] = innerHTML.split(" ");
  const [hours, minutes] = timestamp.split(":");
  return `<li style="width: 5em; padding: 8px 0; float: left; margin-right: 32px;">
      ${hours}:${minutes}
      <span style="color: var(--x-secondary-text-colour);">${am}</span>
    </li>`;
};

class WakeUpCard extends HTMLElement {
  set hass(hass) {
    if (!this.card) {
      this.createCard();
    }

    this.renderHistory();
  }

  createCard() {
    const card = document.createElement("ha-card");
    this.card = card;
    this.content = document.createElement("div");
    this.content.style.padding = "16px 22px";

    card.appendChild(this.content);
    this.appendChild(card);

    this.setTitle = (title) => {
      card.header = title;
      const header = card.shadowRoot.querySelector(".card-header");
      if (header) {
        header.style.padding = "1em 16px";
      }
    };
  }

  renderHistory() {
    const {
      config: { entity, token },
    } = this;

    getHistory(entity, token).then(
      (items) =>
        (this.content.innerHTML = asList(items.map(asListItem).join("")))
    );
  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error("You need to define an entity");
    }
    this.config = config;
  }

  getCardSize() {
    return 3;
  }

  static get styles() {
    return css`
      :host {
        background: red;
      }
    `;
  }
}

customElements.define("wake-up-card", WakeUpCard);
