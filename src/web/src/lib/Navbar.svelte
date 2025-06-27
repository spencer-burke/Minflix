<script>
	let {loggedIn = false} = $props();
</script>

<nav>
	<div class="brand">
		<p>Minflix</p>
	</div>
	<div class="navigation-buttons">
		{#if loggedIn}
			<button>Logout</button>
		{:else}
			<button>Login</button>
			<button>Register</button>
		{/if}
	</div>
</nav> 