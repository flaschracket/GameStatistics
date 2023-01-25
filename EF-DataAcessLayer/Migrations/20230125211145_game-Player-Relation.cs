using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace EFDataAcessLayer.Migrations
{
    /// <inheritdoc />
    public partial class gamePlayerRelation : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<int>(
                name: "GameID",
                table: "players",
                type: "int",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "IX_players_GameID",
                table: "players",
                column: "GameID");

            migrationBuilder.AddForeignKey(
                name: "FK_players_Games_GameID",
                table: "players",
                column: "GameID",
                principalTable: "Games",
                principalColumn: "GameID");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_players_Games_GameID",
                table: "players");

            migrationBuilder.DropIndex(
                name: "IX_players_GameID",
                table: "players");

            migrationBuilder.DropColumn(
                name: "GameID",
                table: "players");
        }
    }
}
