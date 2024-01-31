###
        <script>
        import { onMount } from 'svelte';

        let isModalOpen = false;

        function openModal() {
            isModalOpen = true;
        }

        function closeModal() {
            isModalOpen = false;
        }

        // Fermer la modal si la souris quitte l'icône
        function handleMouseOut() {
            closeModal();
        }

        // Fermer la modal si l'utilisateur clique en dehors de la modal
        onMount(() => {
            window.addEventListener('click', (event) => {
            if (isModalOpen && !event.target.closest('.modal-content')) {
                closeModal();
            }
            });
        });
        </script>

        <style>
        /* Ajoutez le style de votre modal ici */
        .modal {
            display: {isModalOpen ? 'block' : 'none'};
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 20px;
            border: 1px solid #ccc;
        }
        </style>

        <div on:mouseenter={openModal} on:mouseleave={handleMouseOut}>
        <!-- Icône oeil ou tout autre élément déclenchant la modal -->
        <span>👁️</span>

        {#if isModalOpen}
            <div bind:this={modal} on:mouseleave={handleMouseOut} class="modal">
            <!-- Contenu de votre modal -->
            <p>Contenu de la modal</p>
            </div>
        {/if}
        </div>
###