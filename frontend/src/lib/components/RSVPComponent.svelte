<script>
  let rsvpStage = 0;
  let postData = {};
  let responseData = null;

  let foundGuest = false;
  $: guestData = [];

  let name = "";

  $: findGuestData = {
    name: name,
  };

  async function findInvite() {
    rsvpStage += 1;

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/guests/find_guest?format=json",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(findGuestData),
        }
      );

      const responseStatus = response.status;

      if (responseStatus === 200) {
        responseData = await response.json();
        console.log(responseData);
        guestData = responseData;
        foundGuest = true;
      }
    } catch (error) {
      console.log(error);
    }
  }

  async function updateGuestAttendance() {
    rsvpStage += 1;

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/guests/update_guest_attendance?format=json",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(postData),
        }
      );

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  }

  async function updateGuestAccommodation() {
    rsvpStage += 1;

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/guests/update_guest_accommodation?format=json",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(postData),
        }
      );

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  }

  async function updateGuestEmail() {
    rsvpStage += 1;

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/guests/update_guest_accommodation?format=json",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(postData),
        }
      );

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  }

  function increaseRsvpStage() {
    rsvpStage += 1;
  }

  function decreaseRsvpStage() {
    rsvpStage -= 1;
  }
  function handleGuestAttendance(guestID, response) {
    guestData = guestData.map((guest) => {
      if (guest.id === guestID) {
        return { ...guest, attendance: response };
      }
      return guest;
    });
    guestData = [...guestData];
    console.log(guestData);
  }
</script>

<div class="rsvp-wrapper">
  {#if rsvpStage === 0}
    <div class="find-inv-wrapper">
      <p class="rsvp-desc">
        Indien jy vir jou en <span class="comma">'</span>n gas RSVP
        <span class="comma">(</span>of jou familie<span class="comma">),</span>
        sal jy kan RSVP vir die hele groep<span class="comma">.</span>
      </p>
      <div class="form">
        <input
          class="fn-input"
          placeholder="Volle Naam en Van"
          bind:value={name}
        />
        <button class="find-invite-btn" on:click={findInvite}
          >Vind Jou Uitnodiging</button
        >
      </div>
    </div>
  {:else if rsvpStage === 1}
    <div class="found-inv-wrapper">
      {#if foundGuest}
        {#each guestData as guest}
          <div class="guest-wrapper">
            {guest.fullname}
          </div>
        {/each}
        <button class="find-invite-btn" on:click={increaseRsvpStage}
          >Volgende</button
        >
      {/if}
      <button class="find-invite-btn" on:click={decreaseRsvpStage}
        >Soek Weer</button
      >
    </div>
  {:else if rsvpStage === 2}
    <div class="attendance-wrapper">
      Wie kom almal saam<span class="comma">?</span>
      {#each responseData as guest}
        <div class="guest-wrapper">
          {guest.fullname}
          <div class="split-button">
            <button
              class:selected={guest.attendance === 1}
              on:click={() => handleGuestAttendance(guest.id, 1)}>Ja</button
            >
            <button
              class:selected={guest.attendance === 0}
              on:click={() => handleGuestAttendance(guest.id, 0)}>Nee</button
            >
          </div>
        </div>
      {/each}
      <!-- Doen accepted / declined vir al die gaste + vir +1's sit 'n button by om +1 te select, if selected - form field vir naam -->
      <button class="find-invite-btn" on:click={updateGuestAttendance}
        >Volgende</button
      >
      <button class="find-invite-btn" on:click={decreaseRsvpStage}>Terug</button
      >
    </div>
  {:else if rsvpStage === 3}
    <div class="accommodation-wrapper">
      Kies jou verblyf opsies
      <button class="find-invite-btn" on:click={updateGuestAccommodation}
        >Volgende</button
      >
      <button class="find-invite-btn" on:click={decreaseRsvpStage}>Terug</button
      >
    </div>
  {:else if rsvpStage === 4}
    <div class="email-wrapper">
      Epos addres <span class="comma">-</span> baie belangrik sodat Louvain die
      faktuur vir die verblyf na jou kan stuur
      <button class="find-invite-btn" on:click={updateGuestEmail}
        >Volgende</button
      >
      <button class="find-invite-btn" on:click={decreaseRsvpStage}>Terug</button
      >
    </div>
  {:else if rsvpStage === 5}
    <div class="rsvp-done">
      Ons sien uit om ons spesiale dag met julle te deel<span class="comma"
        >!</span
      >

      Daar sal <span class="comma">'</span>n epos gestuur word om die RSVP te
      bevestig<span class="comma">.</span>
    </div>
    <div></div>
  {/if}
</div>

<style>
  .split-button {
    display: flex;
    width: 200px;
    border: 1px solid #ad925d;
    border-radius: 2px;
    overflow: hidden;
  }

  .split-button button {
    flex: 1;
    padding: 10px;
    background-color: azure;
    color: #ad925d;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .split-button button:first-child {
    border-right: 1px solid #ad925d; /* Creates the split effect */
  }

  .split-button button:hover {
    background-color: rgba(173, 146, 93, 0.3);
  }

  .split-button button:active {
    background-color: rgba(173, 146, 93, 0.3);
  }

  .selected {
    background-color: rgba(173, 146, 93, 0.3) !important;
  }

  .rsvp-wrapper {
    border: 1px solid green;
  }

  .found-inv-wrapper,
  .attendance-wrapper,
  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .rsvp-desc {
    border: 1px solid red;
  }

  .form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .fn-input,
  .find-invite-btn {
    margin: 15px 0px 15px 0px;
    width: 450px;
    box-sizing: border-box;
    max-width: 100%;
  }

  .fn-input {
    border: 1px solid #ad925d;
    color: #000;
    background-color: azure;
    font-family: "RoxaleStory";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
    max-width: 100%;
  }

  .fn-input:focus {
    outline: 1px solid #ad925d;
    color: #111;
  }

  .find-invite-btn {
    border: 1px solid #ad925d;
    color: #ad925d;
    background-color: azure;
    cursor: pointer;
    font-family: "RoxaleStory";
    font-size: 22px;
    padding: 8px 20px 8px 20px;
    max-width: 100%;
  }

  .find-invite-btn:hover {
    background-color: azure;
    color: #ad925d;
  }

  .rsvp-desc,
  .attendance-desc,
  .email-desc,
  .rsvp-d-desc {
    font-family: "RoxaleStory";
    color: #ad925d;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    font-size: 20px;
  }

  .comma {
    font-family: "Times New Roman", Times, serif !important;
  }

  @media (min-width: 1000px) {
    .rsvp-desc,
    .attendance-desc,
    .email-desc,
    .rsvp-d-desc {
      font-size: 24px;
    }
  }

  .guest-wrapper {
    display: flex;
    flex-direction: row;
    align-items: first baseline;
  }
</style>
